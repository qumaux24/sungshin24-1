from django.shortcuts import render,redirect, get_object_or_404
from ..models import Noticepost
from ..forms import NoticepostForm
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.db.models import Count
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

# 공지사항 게시글 목록
def noticelist(request):
    fix=Noticepost.objects.filter(id__in=[2, 3])
    noticeposts = Noticepost.objects.all().order_by('-created_at')
    request.session['previous_page']=request.get_full_path()
    page=request.GET.get('page', '1')
    paginator=Paginator(noticeposts, 10)
    page_obj=paginator.get_page(page)
    context={
        'noticelist': page_obj,
        'fix' : fix
        }
    return render(request, 'notice.html', context)

# 공지사항 게시글 새로 작성하기
@login_required
@user_passes_test(lambda u: u.is_superuser)
def noticeWrite(request):
    if request.method=='POST':
        noticeform=NoticepostForm(request.POST)
        if noticeform.is_valid():
            noticepost = noticeform.save(commit=False)
            noticepost.writer=request.user
            noticepost.save()
                
            return redirect('post:noticelist')
    else:
        noticeform=NoticepostForm()
        return render(request,'notice-write.html', {'noticeform':noticeform})
    
# 공지사항 게시글 보여주기
def noticeShow(request, noticepost_id):
    noticepost = get_object_or_404(Noticepost, pk =noticepost_id)
    context = {
        'noticepost': noticepost,
    }
    return render(request, 'notice-detail.html', context)

# # 메인 페이지 공지사항 고정 공지 2개
def sort_notice_fix(request):
    #고정 공지 2개
    return Noticepost.objects.filter(id__in=[2, 3])


# # 메인 페이지 공지사항 일반 공지 2개
def sort_notice(request):    
    return Noticepost.objects.order_by('-created_at')[:2]