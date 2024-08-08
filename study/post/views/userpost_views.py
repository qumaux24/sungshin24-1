from django.shortcuts import render,redirect, get_object_or_404
from ..models import Userpost, Comment
from ..forms import UserpostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator

# Create your views here.

# 사용자 게시글 목록
def userlist(request):
    userposts = Userpost.objects.all().order_by('-created_at')
    request.session['previous_page']=request.get_full_path()
    page=request.GET.get('page', '1')
    paginator=Paginator(userposts, 10)
    page_obj=paginator.get_page(page)
    context={
        'userlist': page_obj,
        }
    return render(request, 'userpost.html', context)

# 사용자 게시글 새로 작성하기
def userWrite(request):
    if request.method=='POST':
        userform=UserpostForm(request.POST)
        if userform.is_valid():
            userpost = userform.save(commit=False)
            userpost.writer=request.user
            userpost.save()
                
            return redirect('userpost:userlist')
    else:
        userform=UserpostForm()
        return render(request,'userpost_write.html', {'userform':userform})
    
# 사용자 게시글 보여주기
def userShow(request, userpost_id):
    userpost = get_object_or_404(Userpost, pk =userpost_id)
    comments = userpost.comment_set.all()  
    commentForm = CommentForm() 
    context = {
        'userpost': userpost,
        'comments': comments,
        'commentForm': commentForm, 
    }
    return render(request, 'userpost_detail.html', context)

# 좋아요 기능
@require_POST
def userlikes(request, userpost_pk):
    if request.user.is_authenticated:
        userpost=get_object_or_404(Userpost, pk=userpost_pk)
        if userpost.like_users.filter(pk=request.user.pk).exists():
            userpost.like_users.remove(request.user)
        else:
            userpost.like_users.add(request.user)
        return redirect('userpost:userShow', userpost_pk)
    return redirect('accounts/login')