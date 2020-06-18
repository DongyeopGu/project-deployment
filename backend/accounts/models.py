from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    
    last_login = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.username
