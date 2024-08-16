from django.shortcuts import render,redirect, get_object_or_404
from ..models import Post, Image, Comment, Userpost, Noticepost
from ..forms import PostForm, CommentForm, UserpostForm, NoticepostForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from accounts.models import User_detail, Pass_keyword
from accounts.forms import UserdetailForm, PasskeywordForm
from django.db.models import Q, Count
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest, HttpResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import make_password

def mypage(request, writer_id):
    if request.user.is_authenticated:
        myposts=MY_myposts(request, writer_id)
        mylikes=MY_mylikes(request, writer_id)
        mycomments=MY_mycomments(request, writer_id)
        
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
            gender = user_detail.gender
            age = user_detail.age
            residence = user_detail.residence
            allergies=set(user_detail.allergies.replace(',',' ').split())
            allergies=list(allergies)
            context = {
                'user_detail': user_detail,
                'allergies' : allergies,
                'gender' : gender,
                'age' : age,
                'residence' : residence,
                'writer_id': writer_id,
            }
            return render(request, 'user_detail_select.html', context )
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

def changelogin(request):
    if request.method == 'POST':
        inputID = request.POST.get('inputID2', '').strip()
        inputkeyword = request.POST.get('inputkeyword2', '').strip()
        newID = request.POST.get('newID', '').strip()
        new_password1 = request.POST.get('new_password3', '').strip()
        new_password2 = request.POST.get('new_password4', '').strip()
        user = User.objects.get(username=inputID)
        pass_keyword = Pass_keyword.objects.get(user=user)           
        if pass_keyword.pass_keyword == inputkeyword :
            if new_password1 == new_password2:
                user.username = newID
                user.password = make_password(new_password1)
                user.save()
                update_session_auth_hash(request, user)
            
                return redirect('post:main')
            else:
                return HttpResponse("비밀번호가 올바르지 않습니다.")
        else:
            return HttpResponse("패스키가 일치하지 않습니다.")
        return redirect('accounts:findPW')
    else:
        
        return render(request, 'changelogin.html')


def user_detail_show(request, writer_id):
    user_detail=get_object_or_404(User_detail, user_id=writer_id)
    gender = user_detail.gender
    age = user_detail.age
    residence = user_detail.residence
    allergies=set(user_detail.allergies.replace(',',' ').split())
    allergies=list(allergies)
    context = {
        'user_detail': user_detail,
        'allergies' : allergies,
        'gender' : gender,
        'age' : age,
        'residence' : residence,
        'writer_id': writer_id,
    }
    return render(request, 'user_detail_select.html', context)