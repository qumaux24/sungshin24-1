from django.shortcuts import render,redirect, get_object_or_404
from ..models import Post, Image
from ..forms import PostForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator

# Create your views here.

# 게시글 수정, 삭제
@login_required(login_url='/accounts/login')
def deleteget(request, post_id):
    post=Post.objects.get(id=post_id)
    post.delete()
    return redirect('post:list')

def updateget(request, post_id):
    post=Post.objects.get(pk=post_id)
    images=Image.objects.filter(post=post)
    if request.method=='POST':
        postForm=PostForm(request.POST, request.FILES.getlist('image'), instance=post)
        
        if postForm.is_valid():
            postForm.save()
            for img in request.FILES.getlist('new_image',None):
                Image.objects.create(post=post, image=img)
            #수정을 했을 경우에만 작성시간 밑에 수정시간이 뜨게
            return redirect('post:show', post_id)
    else:
        postForm=PostForm(instance=post)
        context={
            'postForm':postForm,
            'post_id':post_id,
            'images':images,
        }
        return render(request, 'updated.html', context)                

# 이미지 삭제
def image_delete(request, post_id):
    if request.user.is_authenticated:
        post=get_object_or_404(Post, pk=post_id)
        image_id=request.POST.get('image_id')
        image=get_object_or_404(Image, id=image_id, post=post)
        if request.user == post.writer:
            image.delete()
    return redirect('post:show', post_id=post_id)