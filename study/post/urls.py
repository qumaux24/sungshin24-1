from django.urls import path
from .views.post_views import main, write, show
from .views.notice_views import notice, noticewrite, noticeshow
from .views.userpost_views import userpost, userpostwrite, userpostshow

app_name="post"

urlpatterns = [
    path('', main, name='main'),
    path('write/', write, name='write'),
    path('show/', show, name='show'),
    path('notice/', notice, name='notice'),
    path('noticewrite/', noticewrite, name='noticewrite'),
    path('noticeshow/', noticeshow, name='noticeshow'),
    path('userpost/', userpost, name='userpost'),
    path('userpostwrite/', userpostwrite, name='userpostwrite'),
    path('userpostshow/', userpostshow, name='userpostshow'),
    
    ]
