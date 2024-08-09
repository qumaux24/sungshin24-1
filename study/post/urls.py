from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views.post_views import main, list, write, show, likes
from .views.update_views import updateget, deleteget, image_delete
from .views.comments_views import comments_create, comments_delete
from .views.userpost_views import userWrite, userShow, userlist, userlikes
from .views.userpost_update_views import userpost_deleteget, userpost_updateget
from .views.notice_views import noticeWrite, noticeShow, noticelist
from .views.notice_update_views import noticepost_deleteget, noticepost_updateget
from .views.daily_views import daily_posts_view

app_name="post"

urlpatterns = [
    path('', main, name='main'),
    path('write/', write, name='write'),
    path('show/<int:post_id>/', show, name='show'),
    path('show/<int:post_id>/updateget', updateget, name='updateget'),
    path('deleteget/<int:post_id>/<str:category_name>/', deleteget, name='deleteget'),
    path('<int:pk>/comments/', comments_create, name='comments_create'),
    path('<int:pk>/comments/<int:comment_pk>/delete/', comments_delete, name='comments_delete'),
    path('<int:post_pk>/likes/', likes, name='likes'),
    path('updateget/image_delete/<int:post_id>/', image_delete, name='image_delete'),
    path('userlist/', userlist, name='userlist'),
    path('userWrite/', userWrite, name='userWrite'),
    path('userShow/<int:userpost_id>', userShow, name='userShow'),
    path('userShow/<int:userpost_id>/userpost_updateget', userpost_updateget, name='userpost_updateget'),
    path('userpost_deleteget/<int:userpost_id>/', userpost_deleteget, name='userpost_deleteget'),
    path('<int:userpost_pk>/userlikes/', userlikes, name='userlikes'),
    path('noticelist/', noticelist, name='noticelist'),
    path('noticeWrite/', noticeWrite, name='noticeWrite'),
    path('noticeShow/<int:noticepost_id>', noticeShow, name='noticeShow'),
    path('noticeShow/<int:noticepost_id>/noticepost_updateget', noticepost_updateget, name='noticepost_updateget'),
    path('noticepost_deleteget/<int:noticepost_id>/', noticepost_deleteget, name='noticepost_deleteget'),
    path('<str:category_name>/',list, name='list'),
    path('daily_posts/', daily_posts_view, name='daily_posts'),
    ]

urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)