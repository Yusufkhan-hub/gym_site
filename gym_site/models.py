from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class signUp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

# class gallery(models.Model):
#     photo = models.ImageField()

class feedback(models.Model):
    name=models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=1000)