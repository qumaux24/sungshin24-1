from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views.post_views import main, list, write, show, likes
from .views.update_views import updateget, deleteget, image_delete
from .views.comments_views import comments_create, comments_delete

app_name="post"

urlpatterns = [
    path('', main, name='main'),
    path('list/', list, name='list'),
    path('write/', write, name='write'),
    path('show/<int:post_id>/', show, name='show'),
    path('show/<int:post_id>/updateget', updateget, name='updateget'),
    path('deleteget/<int:post_id>/', deleteget, name='deleteget'),
    path('<int:pk>/comments/', comments_create, name='comments_create'),
    path('<int:pk>/comments/<int:comment_pk>/delete/', comments_delete, name='comments_delete'),
    path('<int:post_pk>/likes/', likes, name='likes'),
    path('updateget/image_delete/<int:post_id>/', image_delete, name='image_delete'),
    ]

urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)