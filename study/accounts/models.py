from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class User_detail(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
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