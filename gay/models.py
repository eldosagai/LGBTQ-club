from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=100,blank=True)
    surname = models.CharField(max_length=100,blank=True)
    email = models.CharField(max_length=100,unique=True)
 

    def __str__(self):
        return self.username