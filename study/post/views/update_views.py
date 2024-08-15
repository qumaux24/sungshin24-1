from django.shortcuts import render,redirect, get_object_or_404
from ..models import Post, Image, Category
from ..forms import PostForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator

# Create your views here.

# 게시글 수정, 삭제
@login_required(login_url='/accounts/login')
def deleteget(request, post_id, category_name):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    allowed_categories = ["koreapost", "chinapost", "japanpost"]

    # 카테고리 이름이 허용된 목록에 있는 경우 해당 카테고리로 리디렉션
    if category_name in allowed_categories:
        return redirect('post:list', category_name=category_name)
    
    # 허용되지 않은 카테고리 이름인 경우 404 페이지 표시
    return render(request, '404.html')

def updateget(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    images = Image.objects.filter(post=post)  # 포스트와 연결된 이미지 가져오기

    if request.method == 'POST':
        postForm = PostForm(request.POST, request.FILES, instance=post)  # request.FILES로 파일 처리

        if postForm.is_valid():
            post = postForm.save()  # 포스트 저장

            # 새로 추가된 이미지 처리
            new_images = request.FILES.getlist('new_image', [])
            if new_images:
                for img in new_images:
                    Image.objects.create(post=post, image=img)
            else:
                if not images.exists():
                    error_message = '이미지 하나 이상을 추가해야 합니다.'
                    return render(request, 'updated.html', {
                        'postForm': postForm,
                        'post_id': post_id,
                        'images': images,
                        'error_message': error_message,
                    })


            return redirect('post:show', post_id=post_id)

    else:
        postForm = PostForm(instance=post)
    
    context = {
        'postForm': postForm,
        'post_id': post_id,
        'images': images,
    }
    return render(request, 'updated.html', context)        


def image_delete(request, post_id):
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        image = get_object_or_404(Image, id=image_id, post_id=post_id)
        image.delete()

        # 삭제 후 포스트의 이미지 수 확인
        post = get_object_or_404(Post, id=post_id)
        
    return redirect('post:updateget', post_id=post_id)