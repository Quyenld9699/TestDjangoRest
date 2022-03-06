from django.contrib import admin

from .models import Blog, Car
# Register your models here.

admin.site.register((Blog, Car,))