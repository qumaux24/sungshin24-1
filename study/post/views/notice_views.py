from django.shortcuts import render, redirect

def notice(request):
    return render(request, 'notice.html')

def noticewrite(request):
    return render(request, 'notice_write.html')

def noticeshow(request):
    return render(request, 'notice_detail.html')