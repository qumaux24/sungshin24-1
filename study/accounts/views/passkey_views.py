from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from ..models import User_detail, Pass_keyword
from ..forms import UserdetailForm, PasskeywordForm
from django.http import HttpResponseBadRequest, HttpResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import make_password

def Passkey(request):
    if request.method=="POST":
        passkeyword=PasskeywordForm(request.POST)
        if passkeyword.is_valid():
            passkeywords = passkeyword.save(commit=False)
            passkeywords.user = request.user
            passkeywords.save()
        return redirect('accounts:user_detail')
    else:
        passkeyword=PasskeywordForm()
        return render(request, 'passkey.html',{'passkeyword':passkeyword})