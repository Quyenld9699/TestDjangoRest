from django.contrib import admin

# Register your models here.
from .models import ModelX, ModelY, TestModel

admin.site.register((TestModel, ModelX, ModelY))