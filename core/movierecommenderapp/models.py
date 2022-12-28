from django.db import models

# Create your models here.

class Show(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=50)
    rated = models.CharField(max_length=50)
    released = models.DateField()
    runtime = models.DurationField()
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    writer = models.CharField(max_length=200)
    actors = models.CharField(max_length=200)
    plot = models.TextField()
    language = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    awards = models.CharField(max_length=100)
    poster = models.URLField()
    metascore = models.CharField(max_length=50)
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1)
    imdb_votes = models.PositiveIntegerField()
    imdb_id = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    total_seasons = models.PositiveSmallIntegerField()

class Rating(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='ratings')
    source = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
