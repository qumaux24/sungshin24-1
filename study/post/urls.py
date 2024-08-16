from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views.post_views import main, list, write, show, likes
from .views.search_views import search, user_search, outsearch, notice_search, notice_outsearch, Catesearch
from .views.update_views import updateget, deleteget, image_delete
from .views.comments_views import comments_create, comments_delete, userComments_create, userComments_delete
from .views.userpost_views import userWrite, userShow, userlist, userlikes
from .views.userpost_update_views import userpost_deleteget, userpost_updateget
from .views.notice_views import noticeWrite, noticeShow, noticelist
from .views.notice_update_views import noticepost_deleteget, noticepost_updateget
from .views.daily_views import daily_posts_view
from .views.mypage_views import mypage, mypage_select, passkey, user_updated, changelogin, user_detail_show

app_name="post"

urlpatterns = [
    #유저디테일
    path('userupdate/<int:writer_id>/', user_updated, name='user_updated'),
    path('changelogin/', changelogin, name="changelogin"),
    #레시피
    path('', main, name='main'),
    path('write/', write, name='write'),
    path('show/<int:post_id>/', show, name='show'),
    path('outsearch/', outsearch, name='outsearch'),
    path('noticeoutsearch/', notice_outsearch, name='notice_outsearch'),
    
    #마이페이지
    path('mypage/<int:writer_id>/', mypage, name='mypage'),
    path('mypage/<int:writer_id>/mypage_select', mypage_select, name="mypage_select"),
    path('mypage/user_detail_show/<int:writer_id>/', user_detail_show, name='user_detail_show'),
    #수정
    path('show/<int:post_id>/updateget', updateget, name='updateget'),
    path('deleteget/<int:post_id>/<str:category_name>/', deleteget, name='deleteget'),
    path('updateget/image_delete/<int:post_id>/', image_delete, name='image_delete'),
    #댓글
    path('<int:pk>/comments/', comments_create, name='comments_create'),
    path('<int:pk>/comments/<int:comment_pk>/delete/', comments_delete, name='comments_delete'),
    #좋아요
    path('<int:post_pk>/likes/', likes, name='likes'),
    #사용자게시판
    path('userlist/', userlist, name='userlist'),
    path('userWrite/', userWrite, name='userWrite'),
    path('userShow/<int:userpost_id>', userShow, name='userShow'),
    # path('userShow/<int:userpost_id>/userpost_updateget', userpost_updateget, name='userpost_updateget'),
    path('<int:userpost_pk>/userlikes/', userlikes, name='userlikes'),
    path('<int:pk>/usercomments/', userComments_create, name='userComments_create'),
    path('<int:pk>/usercomments/<int:usercomment_pk>/delete/', userComments_delete, name='userComments_delete'),
    path('userShow/<int:userpost_id>/userpost_updateget/', userpost_updateget, name='userpost_updateget'),
    path('userpost/delete/<int:userpost_id>/', userpost_deleteget, name='userpost_deleteget'),
    
    #공지사항게시판
    path('noticelist/', noticelist, name='noticelist'),
    path('noticeWrite/', noticeWrite, name='noticeWrite'),
    path('noticeShow/<int:noticepost_id>', noticeShow, name='noticeShow'),
    path('noticeShow/<int:noticepost_id>/noticepost_updateget', noticepost_updateget, name='noticepost_updateget'),
    path('noticepost_deleteget/<int:noticepost_id>/', noticepost_deleteget, name='noticepost_deleteget'),
    #목록
    path('<str:category_name>/',list, name='list'),
    #데일리
    path('daily_posts/', daily_posts_view, name='daily_posts'),
    #패스키
    path('passkey/<int:writer_id>/', passkey, name="passkey"),
    #검색
    path('search/<int:writer_id>/', search, name='search'),
    path('noticesearch/<int:writer_id>/', notice_search, name='notice_search'),
    path('catesearch/<int:writer_id>/<str:category_name>/', Catesearch, name="catesearch"),
    path('usersearch/<int:writer_id>/', user_search, name='user_search'),
    ]

urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)