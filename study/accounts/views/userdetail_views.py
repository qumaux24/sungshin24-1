from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from ..models import User_detail, Pass_keyword
from ..forms import UserdetailForm, PasskeywordForm
from django.http import HttpResponseBadRequest, HttpResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import make_password

def user_detail(request):
    if request.method=="POST":
        user_details_form=UserdetailForm(request.POST)
        if user_details_form.is_valid():
            user_details = user_details_form.save(commit=False)
            user_details.user = request.user
            user_details.save()
        return redirect('post:main')
    else:
        user_details=UserdetailForm()
        return render(request, 'accInfo.html',{'user_details':user_details})

    

