from django.db import models

"""
char (strings)
int (int)
float (decimal point numbers)
boolean (true/false)

"""


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):

    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    in_stock = models.IntegerField()
    price = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    director = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Series(models.Model):
    class Meta:
        verbose_name_plural = "Series"

    title = models.CharField(max_length=90)
    seasons = models.IntegerField()
    episodes = models.IntegerField()
    release_year = models.IntegerField()
    in_stock = models.IntegerField()
    price = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    director = models.CharField(max_length=255)
