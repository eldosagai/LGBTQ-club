import email
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100,blank=True)
    surname = models.CharField(max_length=100,blank=True)
    email = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.username