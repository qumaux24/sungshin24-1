from django.shortcuts import render,redirect, get_object_or_404
from ..models import Post, Image, Comment, Category
from ..forms import PostForm, CommentForm
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.db.models import Count, Q
from .daily_views import daily_posts_view
# from django.contrib.auth import get_user_model

# Create your views here.

# 메인페이지
def main(request):
    context = daily_posts_view(request)
    print(context)
    return render(request, 'main.html', context)

# 게시글 목록
def list(request, category_name):
    request.session['previous_page'] = request.get_full_path()
    category = get_object_or_404(Category, name=category_name)
    posts = Post.objects.filter(category=category).annotate(comment_count=Count('comment')).order_by('-created_at').order_by('-created_at')
    page=request.GET.get('page', '1')
    paginator=Paginator(posts, 10)
    page_obj=paginator.get_page(page)
    context={
        'list': page_obj,
        }
    if category_name=="koreapost":
        return render(request, 'koreapost.html', context)
    elif category_name=="chinapost":
        return render(request, 'chinapost.html', context)
    elif category_name=="japanpost":
        return render(request, 'japanpost.html', context)
    else:
        return render(request, '404.html')

# 게시글 새로 작성하기
def write(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer=request.user
            
            if post.category is None:
                # 카테고리가 없는 경우 기본값 설정 또는 오류 처리
                return render(request, 'write.html', {'post_form': form, 'error': '카테고리를 선택하세요.'})
            
            post.save()
            
            for img in request.FILES.getlist('image',None):
                Image.objects.create(post=post, image=img)
                
            return redirect('post:list', category_name=post.category.name)
        
    else:
        form=PostForm() #request는 현재 상황인데 없으니까 아예 새 포스트를 불러옴
        return render(request,'recipeRegistration.html', {'form':form})

# 게시글 보여주기
def show(request, post_id):
    post = get_object_or_404(Post, pk =post_id)
    images=Image.objects.filter(post=post)
    comments = post.comment_set.all()  
    commentForm = CommentForm() 
    context = {
        'post': post,
        'images': images,
        'comments': comments,
        'commentForm': commentForm, 
    }
    return render(request, 'recipepage.html', context)

# 좋아요 기능
@require_POST
def likes(request, post_pk):
    if request.user.is_authenticated:
        post=get_object_or_404(Post, pk=post_pk)
        if post.like_users.filter(pk=request.user.pk).exists():
            post.like_users.remove(request.user)
        else:
            post.like_users.add(request.user)
        return redirect('post:show', post_pk)
    return redirect('accounts/login')


# 검색 기능
def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        search_word = set(searched.replace(',', ' ').split())
        
        q_objects = Q()
        for word in search_word:
            if word:  # 빈 문자열 필터링
                q_objects |= Q(title__icontains=word) | Q(ingredient__icontains=word)
        
        # 검색 수행
        posts = Post.objects.filter(q_objects).distinct()
        
    context = {
        'searched':searched,
        'posts':posts
    }    
    
    return render(request, 'searched.html', context)