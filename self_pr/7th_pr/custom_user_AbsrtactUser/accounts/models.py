from django.db import models
from .manager import UserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    username = None         #we used this to not use the username field
    phone_number = models.BigIntegerField(blank=False,unique=True)
    email =models.EmailField(unique=True)
    user_bio = models.CharField(max_length=50)
    user_profile_img =models.ImageField(upload_to="profile")
     
    USERNAME_FIELD = 'phone_number'     #it is used to assign username to new field i.e what we want to use instead of username
    REQUIRED_FIELDS = []
    objects =UserManager()
    