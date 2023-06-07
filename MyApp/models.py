from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    bio=models.CharField(max_length=200)
    avatar=models.ImageField(null=True)
    work_location=models.IntegerField()
    time_zone=models.CharField(max_length=10)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='posts')
