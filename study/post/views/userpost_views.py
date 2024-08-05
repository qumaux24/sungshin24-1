from django.shortcuts import render, redirect

def userpost(request):
    return render(request, 'userpost.html')

def userpostwrite(request):
    return render(request, 'userpost_write.html')

def userpostshow(request):
    return render(request, 'userpost_detail.html')