from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    confirm_password=models.CharField(max_length=100,null=True,blank=True)