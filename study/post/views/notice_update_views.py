from django.shortcuts import render,redirect, get_object_or_404
from ..models import Noticepost, Comment
from ..forms import NoticepostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator

# Create your views here.

# 공지사항 게시글 수정, 삭제
@login_required(login_url='/accounts/login')
def noticepost_deleteget(request, noticepost_id):
    noticepost=Noticepost.objects.get(id=noticepost_id)
    noticepost.delete()
    return redirect('post:noticelist')

def noticepost_updateget(request, noticepost_id):
    noticepost=Noticepost.objects.get(pk=noticepost_id)
    if request.method=='POST':
        noticepostForm=NoticepostForm(request.POST, instance=noticepost)
        
        if noticepostForm.is_valid():
            noticepostForm.save()
            
            return redirect('post:noticeShow', noticepost_id)
    else:
        noticepostForm=NoticepostForm(instance=noticepost)
        context={
            'noticepostForm':noticepostForm,
            'noticepost_id':noticepost_id,
        }
        return render(request, 'notice-update.html', context)                