from django.db import models
from django.conf import settings
from movies.models import Movie
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    