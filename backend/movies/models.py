from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name


class Movie(models.Model):
    adult = models.BooleanField(null=True)
    backdrop_path = models.CharField(max_length=500, null=True)
    genres = models.ManyToManyField(Genre, related_name='movie_genre')
    original_title = models.CharField(max_length=300)
    original_language = models.CharField(max_length=300)
    overview = models.TextField()
    release_date = models.DateField(blank=True)
    popularity = models.FloatField(blank=True, null=True)
    poster_path = models.CharField(max_length=500, null=True)
    title = models.CharField(max_length=300)
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    def __str__(self):
        return self.title
        
class Review(models.Model): # 영화 Review 저장 모델
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)    # movie와 1:N관계
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
