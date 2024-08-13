from django.shortcuts import render,redirect, get_object_or_404
from ..models import Post, Image, Comment, Userpost, Noticepost
from ..forms import PostForm, CommentForm, UserpostForm, NoticepostForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from accounts.models import User_detail, Pass_keyword
from accounts.forms import UserdetailForm
from django.db.models import Q, Count

def mypage(request, writer_id):
    if request.user.is_authenticated:
        myposts=MY_myposts(request, writer_id)
        mylikes=MY_mylikes(request, writer_id)
        mycomments=MY_mycomments(request, writer_id)
        
        page=request.GET.get('page', '1')
        paginator=Paginator(myposts, 5)
        myposts=paginator.get_page(page)
            
        page=request.GET.get('page', '1')
        paginator=Paginator(mylikes, 5)
        mylikes=paginator.get_page(page)
        
        page=request.GET.get('page', '1')
        paginator=Paginator(mycomments, 5)
        mycomments=paginator.get_page(page)

        context={
                'myposts' : myposts,
                'mylikes' : mylikes,
                'mycomments' : mycomments,
                # {'selected_page' : selected_page},

            }
        return render(request, 'mypage.html', context)
    else:
        return redirect('accounts:login')

def mypage_select(request, writer_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            selected_page = request.POST.get('page')
            myposts=MY_myposts(request, writer_id)
            mylikes=MY_mylikes(request, writer_id)
            mycomments=MY_mycomments(request, writer_id)
            
            page=request.GET.get('page', '1')
            paginator=Paginator(myposts, 5)
            myposts=paginator.get_page(page)
            
            page=request.GET.get('page', '1')
            paginator=Paginator(mylikes, 5)
            mylikes=paginator.get_page(page)
            
            page=request.GET.get('page', '1')
            paginator=Paginator(mycomments, 5)
            mycomments=paginator.get_page(page)
            
            context={
                'selected_page' : selected_page,
                'myposts' : myposts,
                'mylikes' : mylikes,
                'mycomments' : mycomments,
                # 'selected_page' : selected_page,

            }
            return render(request, 'mypage.html', context)
        else:
            return redirect('post:mypage', writer_id=writer_id)
            # 여기서 선택한 값에 따라 적절한 로직을 처리할 수 있습니다.
            # 예를 들어, 다른 페이지로 리다이렉트할 수 있습니다.
            # return HttpResponse(f"Selected page: {selected_page}")
        return render(request, 'mypage.html')
    else:
        return redirect('accounts:login')

User = get_user_model()

def MY_myposts(request, writer_id):
    user = User.objects.get(pk=writer_id)
    if request.user.pk == user.pk:
        myposts = Post.objects.filter(writer=user).annotate(comment_count=Count('comment')).order_by('-created_at')
    return myposts

def MY_mylikes(request, writer_id):
    user = User.objects.get(pk=writer_id)
    if request.user.pk == user.pk:
        mylikes = Post.objects.filter(like_users=user).annotate(comment_count=Count('comment')).order_by('-created_at')
    return mylikes

def MY_mycomments(request, writer_id):
    user = User.objects.get(pk=writer_id)
    if request.user.pk == user.pk:
        mycomments = Post.objects.filter(comment__writer=user).distinct().annotate(comment_count=Count('comment')).order_by('-created_at')
    return mycomments

def passkey(request, writer_id):
    user = User.objects.get(pk=writer_id)
    if request.user.pk == user.pk:
        inputpasskey=request.POST['inputpasskey']
        pass_key=Pass_keyword.objects.filter(user_id=user.id)
        pass_key_value = pass_key.first().pass_keyword if pass_key.exists() else None
        if inputpasskey==pass_key_value:
            user_detail=get_object_or_404(User_detail, user_id=writer_id)
            return render(request, 'user_detail_select.html', {'writer_id': writer_id} )
        return redirect('post:mypage', writer_id)
    return redirect('post:main')

def user_updated(request, writer_id):
    user_detail = User_detail.objects.get(user_id=writer_id)
    if request.method=="POST":
        user_update_form=UserdetailForm(request.POST, instance=user_detail)
        if user_update_form.is_valid():
            print('유저디테일폼 유효함')
            # post.created_at=post.updated_at
            user_detail.user=request.user
            user_update_form.save()
            
        return redirect('post:user_detail_show',  writer_id=writer_id)
        # return redirect('post:user_detail_show', writer_id=writer_id)
    else:
        user_update_form = UserdetailForm(instance=user_detail)

        context = {
            'user_update_form': user_update_form,
            'user_detail' : user_detail,
            'writer_id':writer_id
        }
        return render(request,'membership.html',context)

# def user_detail_show(request, writer_id):
#     user_detail=get_object_or_404(User_detail, writer_id=writer_id)
#     allergies=set(user_detail.allergy.replace(',',' ').split())
#     allergies=list(allergies)
#     context = {
#         'user_detail': user_detail,
#         'allergies' : allergies
#     }
#     return render(request, 'user_detail2.html', context)