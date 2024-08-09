from django.contrib import admin
from .models import Noticepost

# Register your models here.

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