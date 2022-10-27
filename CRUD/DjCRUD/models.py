from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    first_name=models.CharField(max_length=100,null=False,blank=False)
    last_name=models.CharField(max_length=100,null=False,blank=False)
    email=models.EmailField(max_length=100,null=False,blank=False,unique=True)
    

class Address(models.Model):
    user= models.OneToOneField(Users, on_delete=models.CASCADE)
    address1=models.CharField(max_length=215,null=False,blank=False,unique=True)
    address2=models.CharField(max_length=215,null=True,blank=True)
    phonenumber=models.IntegerField(null=False,blank=False,unique=True)
    city=models.CharField(max_length=215,null=True,blank=True)
    postel_code=models.IntegerField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at=models.DateTimeField(auto_now=True,null=True, blank=True)
