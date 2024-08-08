from django import forms
from .models import Post, Comment, Userpost, Noticepost

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title', 'cooktime', 'ingredient', 'cookmethod']
        
class UserpostForm(forms.ModelForm):
    class Meta:
        model=Userpost
        fields=['title','content']
        
class NoticepostForm(forms.ModelForm):
    class Meta:
        model=Noticepost
        fields=['title', 'content']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['comment']