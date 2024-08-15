from django.shortcuts import render,redirect, get_object_or_404
from ..models import Post, Image, Comment, Userpost, Noticepost, Usercomment
from ..forms import PostForm, CommentForm, UserpostForm, NoticepostForm, UsercommentForm
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
        usercommentForm=UsercommentForm(request.POST)
        if usercommentForm.is_valid():
            usercomment=usercommentForm.save(commit=False)
            usercomment.post=userpost
            usercomment.writer=request.user
            usercomment.save()
        return redirect('post:userShow', pk)
    return redirect('accounts/login')

@require_POST
def userComments_delete(request, pk, usercomment_pk):
    if request.user.is_authenticated:
        usercomment = get_object_or_404(Usercomment, pk=usercomment_pk)
        if request.user == usercomment.writer:
            usercomment.delete()
    return redirect('post:userShow', pk)