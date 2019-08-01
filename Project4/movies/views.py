from django.shortcuts import render
from django.http import HttpResponse
from django.db import models

from .models import Genre, Movie


"""


"""


def index(request):
    all_movies = Movie.objects.all()
    return render(request, 'views/index.html', {'title': 'Home', 'catalog': all_movies})


def about(request):

    return render(request, 'views/about.html', {'name': 'Paul'})


def read_test(request):
    all = Genre.objects.all()
    print(all)
    names = ''
    for g in all:
        names += g.name

    return HttpResponse(names)
