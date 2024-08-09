from django.shortcuts import render,redirect, get_object_or_404
from ..models import Noticepost, Image, Comment
from ..forms import NoticepostForm, CommentForm
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST

# Create your views here.

# 공지사항 게시글 목록
def noticelist(request):
    noticeposts = Noticepost.objects.all().order_by('-created_at')
    request.session['previous_page']=request.get_full_path()
    page=request.GET.get('page', '1')
    paginator=Paginator(noticeposts, 10)
    page_obj=paginator.get_page(page)
    context={
        'noticelist': page_obj,
        }
    return render(request, 'notice.html', context)

# 공지사항 게시글 새로 작성하기
def noticeWrite(request):
    if request.method=='POST':
        noticeform=NoticepostForm(request.POST)
        if noticeform.is_valid():
            noticepost = noticeform.save(commit=False)
            noticepost.writer=request.user
            noticepost.save()
                
            return redirect('noticepost:noticelist')
    else:
        noticeform=NoticepostForm()
        return render(request,'notice-write.html', {'noticeform':noticeform})
    
# 공지사항 게시글 보여주기
def noticeShow(request, noticepost_id):
    noticepost = get_object_or_404(Noticepost, pk =noticepost_id)
    comments = noticepost.comment_set.all()  
    commentForm = CommentForm() 
    context = {
        'noticepost': noticepost,
        'comments': comments,
        'commentForm': commentForm, 
    }
    return render(request, 'notice-detail.html', context)