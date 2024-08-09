from django import forms
from .models import Post, Comment, Userpost, Noticepost, Category

class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True, empty_label=None)
    class Meta:
        model=Post
        fields=['title', 'category', 'cooktime', 'ingredient', 'cookmethod']
        
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