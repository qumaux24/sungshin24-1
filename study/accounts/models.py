from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class User_detail(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField()
    RESIDENCE_CHOICES = [
        ('alone', '자취'), 
        ('home', '본가'), 
        ('dormitory', '기숙사'), 
    ]
    residence = models.CharField(max_length=10, default='alone', choices=RESIDENCE_CHOICES, verbose_name="거주지")
    GENDER_CHOICES = [
        ('female', '여자'),
        ('male', '남자'),
        ('ect', '기타')
    ]
    gender = models.CharField(max_length=6, default='ect', choices=GENDER_CHOICES, verbose_name='성별')
    allergy = models.TextField()
    
    def __str__(self):
        # return self.user
        return self.user.username
    
class Pass_keyword(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pass_keyword = models.CharField(max_length=100)
    def __str__(self):
        # return self.user
        return self.user.username