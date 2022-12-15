from django.contrib import admin
from django.contrib.admin import ModelAdmin

from news.models import Blog


# Register your models here.

@admin.register(Blog)
class AdminModel(ModelAdmin):
    class Meta:
        exclude = ('slug',)
