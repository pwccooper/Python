from django.contrib import admin

from .models import Genre, Movie, Series

# Register your models here.


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'in_stock', 'price')
    #exclude = ('in_stock', 'price')
    fields = ('genre', 'title', 'director',
              'in_stock', 'release_year', 'price')


admin.site.register(Genre)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Series)
