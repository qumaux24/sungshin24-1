from django.shortcuts import render,redirect, get_object_or_404
from ..models import Post, Image, Comment, Category
from ..forms import PostForm, CommentForm
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.db.models import Count, Q
from .daily_views import daily_posts_view
# from .notice_views import sort_notice_fix, sort_notice
# from django.contrib.auth import get_user_model

# Create your views here.

# 메인페이지
def main(request):
    context_daily = daily_posts_view(request)
    korea_hot_list = sort_hot_korea(request)
    china_hot_list = sort_hot_china(request)
    japan_hot_list = sort_hot_japan(request)
    # fix_notice = sort_notice_fix(request)
    # main_notice = sort_notice(request)

    context={
        'context_daily' : context_daily,
        'korea_hot_list' : korea_hot_list,
        'china_hot_list' : china_hot_list,
        'japan_hot_list' : japan_hot_list,
        # 'fix_notice': fix_notice,
        # 'main_notice': main_notice,
    }
    return render(request, 'main.html', context)

# 게시글 목록
def list(request, category_name):
    request.session['previous_page'] = request.get_full_path()
    category = get_object_or_404(Category, name=category_name)
    posts = Post.objects.filter(category=category).annotate(comment_count=Count('comment')).order_by('-created_at')
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
# def search(request):
#     if request.method == 'POST':
        
#         if request.method == 'POST':
#             search_select = request.POST.get('search_select')  # 폼에서 선택한 검색 조건을 가져옴
#             searched = request.POST.get('searched', '')
        
#         intermediate_terms = searched.split()
        
#         search_terms = []
#         for term in intermediate_terms:
#             search_terms.extend(term.split(','))

#         search_terms = set(searched.replace(',', ' ').split())
        
#         query = Q()
#         for term in search_terms:
#             if search_select == '제목':
#                 query |= Q(title__icontains=term)
#             elif search_select == '재료':
#                 query |= Q(ingredient__icontains=term)
#             else:
#                 query |= Q(title__icontains=term) | Q(ingredient__icontains=term)
#         posts = Post.objects.filter(query)
#         return render(request, 'searched.html', {'searched': searched, 'posts': posts})
#     else:
#         return render(request, 'searched.html', {})

# 한/중/일식 핫게시판
def sort_hot_korea(request):
    posts = Post.objects.filter(category_id=1).annotate(comment_count=Count('like_users')).order_by('-created_at')
    # posts = Post.objects.all().annotate(comment_count=Count('like_users')).order_by('-created_at')
    page = request.GET.get('page', '1')
    post_likes = []
    
    for post in posts:
        likes_count = post.like_users.all().count()
        post_likes.append((post, likes_count, post.created_at))
        
    post_likes.sort(key=lambda x: (x[1], x[2]), reverse=True)
    sorted_posts_like = [post for post, likes_count, created_at in post_likes]
    
    korea_hot_list = []
    korea_hot_list.append(sorted_posts_like[0])
    korea_hot_list.append(sorted_posts_like[1])

    return korea_hot_list

def sort_hot_china(request):
    posts = Post.objects.filter(category_id=2).annotate(comment_count=Count('like_users')).order_by('-created_at')
    # posts = Post.objects.all().annotate(comment_count=Count('like_users')).order_by('-created_at')
    page = request.GET.get('page', '1')
    post_likes = []
    
    for post in posts:
        likes_count = post.like_users.all().count()
        post_likes.append((post, likes_count, post.created_at))
        
    post_likes.sort(key=lambda x: (x[1], x[2]), reverse=True)
    sorted_posts_like = [post for post, likes_count, created_at in post_likes]
    
    china_hot_list = []
    china_hot_list.append(sorted_posts_like[0])
    china_hot_list.append(sorted_posts_like[1])

    return china_hot_list

def sort_hot_japan(request):
    posts = Post.objects.filter(category_id=3).annotate(comment_count=Count('like_users')).order_by('-created_at')
    # posts = Post.objects.all().annotate(comment_count=Count('like_users')).order_by('-created_at')
    page = request.GET.get('page', '1')
    post_likes = []
    
    for post in posts:
        likes_count = post.like_users.all().count()
        post_likes.append((post, likes_count, post.created_at))
        
    post_likes.sort(key=lambda x: (x[1], x[2]), reverse=True)
    sorted_posts_like = [post for post, likes_count, created_at in post_likes]
    
    japan_hot_list = []
    japan_hot_list.append(sorted_posts_like[0])
    japan_hot_list.append(sorted_posts_like[1])

    return japan_hot_list
