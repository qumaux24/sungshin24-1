from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from ..models import User_detail, Pass_keyword
from ..forms import UserdetailForm, PasskeywordForm
from django.http import HttpResponseBadRequest, HttpResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import make_password

def findPW(request):
    if request.method == 'POST':
        inputID = request.POST.get('inputID', '').strip()
        inputkeyword = request.POST.get('inputkeyword', '').strip()
        new_password1 = request.POST.get('new_password1', '').strip()
        new_password2 = request.POST.get('new_password2', '').strip()
        user = User.objects.get(username=inputID)
        pass_keyword = Pass_keyword.objects.get(user=user)           
        if pass_keyword.pass_keyword == inputkeyword :
            if new_password1 == new_password2:
                user.password = make_password(new_password1)
                user.save()
                update_session_auth_hash(request, user)
            
                return render(request, 'showPW.html')
            else:
                return HttpResponse("비밀번호가 올바르지 않습니다.")
        else:
            return HttpResponse("비밀번호 힌트가 일치하지 않습니다.")
        return redirect('login:findPW')
    else:
        
        return render(request, 'findPW.html')