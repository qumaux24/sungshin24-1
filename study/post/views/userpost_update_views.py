from django.shortcuts import render,redirect, get_object_or_404
from ..models import Userpost, Image
from ..forms import UserpostForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator

# Create your views here.

# 사용자 게시글 수정, 삭제
# @login_required(login_url='/accounts/login')
def userpost_deleteget(request, userpost_id):
    userpost=Userpost.objects.get(id=userpost_id)
    userpost.delete()
    return redirect('post:userlist')

def userpost_updateget(request, userpost_id):
    userpost=Userpost.objects.get(id=userpost_id)
    if request.method=='POST':
        userpostForm=UserpostForm(request.POST, instance=userpost)
        
        if userpostForm.is_valid():
            userpostForm.save()
            
            return redirect('post:userShow', userpost_id)
    else:
        userpostForm=UserpostForm(instance=userpost)
        context={
            'userpostForm':userpostForm,
            'userpost_id':userpost_id,
        }
        return render(request, 'userpost_updated.html', context)                