from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    nickname = models.CharField(max_length=100, unique=True)    
    
    def __str__(self):
        return self.nickname

class DailyNumbers(models.Model):
    date = models.DateField(default=timezone.now)
    daily1 = models.IntegerField()
    daily2 = models.IntegerField()
    daily3 = models.IntegerField()

    def __str__(self):
        return f"{self.date}: {self.daily1}, {self.daily2}, {self.daily3}"
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    cooktime = models.IntegerField()
    ingredient = models.TextField()
    cookmethod = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    writer=models.ForeignKey(User, on_delete=models.CASCADE)
    like_users=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts', blank=True)
    updated_at=models.DateTimeField(null=True, blank=True, auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Userpost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    writer=models.ForeignKey(User, on_delete=models.CASCADE)
    like_users=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_userposts', blank=True)
    updated_at=models.DateTimeField(null=True, blank=True, auto_now=True)
    
    def __str__(self):
        return self.title

class Noticepost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    writer=models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at=models.DateTimeField(null=True, blank=True, auto_now=True)
    
    def __str__(self):
        return self.title
    
class Image(models.Model):
    post=models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    image=models.ImageField(blank=True, upload_to="images/")
    
class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    writer=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment