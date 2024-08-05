from django.shortcuts import render,redirect, get_object_or_404
from ..models import Post, Image, Comment
from ..forms import PostForm, CommentForm
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST

# Create your views here.

# 메인페이지
def main(request):
    return render(request, 'main.html')

# 게시글 목록
def list(request):
    posts = Post.objects.all().order_by('-created_at')
    request.session['previous_page']=request.get_full_path()
    page=request.GET.get('page', '1')
    paginator=Paginator(posts, 10)
    page_obj=paginator.get_page(page)
    context={
        'list': page_obj,
        }
    return render(request, 'koreapost.html', context)

# 게시글 새로 작성하기
def write(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer=request.user
            post.save()
            
            for img in request.FILES.getlist('image',None):
                Image.objects.create(post=post, image=img)
                
            return redirect('post:list')
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