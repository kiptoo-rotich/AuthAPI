from typing import Match
from django.core.files.base import equals_lf
from django.db import models
from django.db.models.fields import EmailField

class Login(models.Model):
    username= models.CharField(max_length=50,null=False)
    password=models.CharField(max_length=25, null=False)

class Register(models.Model):
    username= models.CharField(max_length=50,null=False,unique=True)
    password=models.CharField(max_length=25, null=False)
    repeatpassword=models.CharField(max_length=25, null=False)