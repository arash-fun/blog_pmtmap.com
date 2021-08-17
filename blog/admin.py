from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from django.db import models
from .models import Article 

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display =(
        'title',
        'slug',
        'jpublish',
        'status'
    )

    list_filter =(
        'publish',
        'status'
    )
   
    search_fields = ('title' ,'descriptions')

     #  a property to slug writes title
    prepopulated_fields = {'slug':('title',)}
    # ordering - means decrising order
    ordering = ['-status' , '-publish']


admin.site.register(Article , ArticleAdmin)