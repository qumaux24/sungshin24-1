from django.shortcuts import render,redirect, get_object_or_404
from ..models import Post, Image, Comment, Userpost, Noticepost
from ..forms import PostForm, CommentForm, UserpostForm, NoticepostForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
# Create your views here.

# 댓글 기능
@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        post=Post.objects.get(pk=pk)
        commentForm=CommentForm(request.POST)
        if commentForm.is_valid():
            comment=commentForm.save(commit=False)
            comment.post=post
            comment.writer=request.user
            comment.save()
        return redirect('post:show', pk)
    return redirect('accounts/login')

@require_POST
def comments_delete(request, pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.writer:
            comment.delete()
    return redirect('post:show', pk)

# 사용자 댓글 기능
@require_POST
def userComments_create(request, pk):
    if request.user.is_authenticated:
        userpost=Userpost.objects.get(pk=pk)
        commentForm=CommentForm(request.POST)
        if commentForm.is_valid():
            comment=commentForm.save(commit=False)
            comment.post=userpost
            comment.writer=request.user
            comment.save()
        return redirect('userpost:userShow', pk)
    return redirect('accounts/login')

@require_POST
def userComments_delete(request, pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.writer:
            comment.delete()
    return redirect('userpost:userShow', pk)

# 공지사항 댓글 기능
@require_POST
def noticeComments_create(request, pk):
    if request.user.is_authenticated:
        noticepost=Noticepost.objects.get(pk=pk)
        commentForm=CommentForm(request.POST)
        if commentForm.is_valid():
            comment=commentForm.save(commit=False)
            comment.post=noticepost
            comment.writer=request.user
            comment.save()
        return redirect('noticepost:noticeShow', pk)
    return redirect('accounts/login')

@require_POST
def noticeComments_delete(request, pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.writer:
            comment.delete()
    return redirect('noticepost:noticeShow', pk)