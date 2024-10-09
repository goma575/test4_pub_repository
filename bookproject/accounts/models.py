from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     pass
class CustomUser(AbstractUser):
    address= models.CharField(max_length=100,null=True,blank=True)

