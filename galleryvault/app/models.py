from django.db import models

class user(models.Model):
    username=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

class files(models.Model):
    photos=models.ImageField
# Create your models here.
