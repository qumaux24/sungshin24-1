from django import forms
from .models import Post, Comment, Userpost, Noticepost, Category, Usercomment
from django.forms import TextInput, NumberInput,Textarea

class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True, empty_label=None)
    class Meta:
        model=Post
        fields=['title', 'category', 'cooktime', 'ingredient', 'cookmethod']
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'
                # 'placeholder': 'Name'
                }),
            'cooktime': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'
                # 'placeholder': 'Email'
                }),
            'ingredient': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'
                # 'placeholder': 'Age'
            }),
            'cookmethod': Textarea(attrs={
                'class': "form-control",
                'style': 'width: 500px; height: 500px;'
                # 'placeholder': 'Age'
            }),
        }
        
class UserpostForm(forms.ModelForm):
    class Meta:
        model=Userpost
        fields=['title','content']
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'
                # 'placeholder': 'Name'
                }),
            'content': Textarea(attrs={
                'class': "form-control",
                'style': 'width: 500px; height: 500px;'
                # 'placeholder': 'Age'
            }),
        }
        
class NoticepostForm(forms.ModelForm):
    class Meta:
        model=Noticepost
        fields=['title', 'content']
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'
                # 'placeholder': 'Name'
                }),
            'content': Textarea(attrs={
                'class': "form-control",
                'style': 'width: 500px; height: 500px;'
                # 'placeholder': 'Age'
            }),
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['comment']
        widgets = {
            'comment': Textarea(attrs={
                'class': "form-control",
                'style': 'width: 500px; height: 50px;'
                # 'placeholder': 'Age'
            }),
        }
        
class UsercommentForm(forms.ModelForm):
    class Meta:
        model=Usercomment
        fields=['usercomment']
        widgets = {
            'usercomment': Textarea(attrs={
                'class': "form-control",
                'style': 'width: 500px; height: 50px;'
                # 'placeholder': 'Age'
            }),
        }