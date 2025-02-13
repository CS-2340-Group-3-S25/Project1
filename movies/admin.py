from django.contrib import admin

from .models import Movie, Review

from .models import Movie
from .models import Order


# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']


admin.site.register(Movie, MovieAdmin)

admin.site.register(Review)

admin.site.register(Order)
