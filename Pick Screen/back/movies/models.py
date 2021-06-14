from django.db import models
from django.conf import settings

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, default=0)
    overview = models.TextField()
    poster_path = models.CharField(max_length=100)
    release_date = models.CharField(max_length=100)
    vote_score = models.IntegerField()
    vote_average = models.FloatField(default=0.0)
    vote_count = models.IntegerField(default=0)
    popularity = models.FloatField(default=0.0)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    grade = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

