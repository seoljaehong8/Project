from django.contrib import admin
from .models import Movies, Rating

# Register your models here.
admin.site.register(Movies)
admin.site.register(Rating)