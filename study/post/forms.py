from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    #작성하려고 했을 때 새 폼을 주는 것
    class Meta:
        model=Post
        fields=['title','content']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['comment']