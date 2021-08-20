from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from django.db import models
from .models import Article , Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display =(
        'position',
        'title',
        'slug',
        'parent',
        'status'
    )

    list_filter =(['status'])
   
    search_fields = ('title' ,'slug')
    prepopulated_fields = {'slug':('title',)}
    
    


admin.site.register(Category , CategoryAdmin)



class ArticleAdmin(admin.ModelAdmin):
    list_display =(

        'title',
        'slug',
        'category_to_str',
        'jpublish',
        'status'
    )

    list_filter =(
        'publish',
        'status'
    )
    ordering = ['-publish']
    search_fields = ('title' ,'descriptions')

     #  a property to slug writes title
    prepopulated_fields = {'slug':('title',)}
    # ordering - means decrising order
    ordering = ['-status' , '-publish']
    # for show category here , for manytomanyField
    def category_to_str(self , obj ):
        return ','.join([category.title for category in obj.category_published()])
    category_to_str.short_description = 'دسته بندی'

admin.site.register(Article , ArticleAdmin)
