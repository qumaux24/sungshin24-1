from django.contrib import admin
from .models import Noticepost
from .models import Post

# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_display=('title','cooktime', 'ingredient', 'cookmethod', 'created_at', 'writer', 'updated_at', 'category')
    list_filter=('category',)
    search_fields=('title', 'ingredient', 'writer__user_id',)
    
admin.site.register(Post, PostAdmin)

class NoticeAdmin(admin.ModelAdmin):
    list_display=(
        'title',
        'writer',
        'created_at',
        'updated_at',
    )
    search_fields=('title', 'content', 'writer__user_id',)
    
    def has_add_permission(self, request):
        return request.user.is_superuser
    
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

admin.site.register(Noticepost, NoticeAdmin)