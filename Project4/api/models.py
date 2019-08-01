from django.db import models

from movies.models import Genre, Movie, Series

from tastypie.resources import ModelResource, fields, ALL


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
        filtering = {
            'release_year': ALL,
            'price ': ALL,
            'in_stock': ALL,
            'title': ALL

        }
        ordering: ['release_year', 'price', 'in_stock']
