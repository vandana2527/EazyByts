from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.DateTimeField(auto_now_add=True)
    room = models.CharField(max_length=255, default='general')
    text = models.CharField(max_length=500)