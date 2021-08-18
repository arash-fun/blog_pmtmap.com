from django.db import models
from django.db.models.expressions import OrderBy
from django.db.models.fields.related import create_many_to_many_intermediary_model
from django.utils import timezone
from extensions.utils import jalali_converter
# Create your models here.

# managers in django ,(object is a manager for example)
# my manager
class ArtilceManager(models.Manager):
    def published(self):
        return self.filter(status = 'p')




class Category(models.Model):
    title = models.CharField(max_length=200 , verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=100 ,unique=True ,verbose_name='اسلاگ دسته بندی')
    status = models.BooleanField(default=True, verbose_name='آیا دسته نمایش داده شود؟')
    position = models.IntegerField(verbose_name='پوزیشن')
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسنه بندی ها'
        ordering =['position'] 
    def __str__(self):
        return self.title


class Article(models.Model):
    STATUS_CHOICES =(
        # ('d','Draft'),
        # ('p','Published'),
        ('d','پیش نویس'),
        ('p','منتشر شده'),
    )
    title = models.CharField(max_length=255 , verbose_name='عنوان')
    slug = models.SlugField(max_length=100 , unique=True,verbose_name='اسلاگ')
    category = models.ManyToManyField(Category,verbose_name='دسته بندی', related_name='articles')
    descriptions = models.TextField(verbose_name='توضیحات')
    thumbnail = models.ImageField(upload_to='images' ,blank = True, null=True , verbose_name='تصویر')
    publish = models.DateTimeField(default=timezone.now , verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True , verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True , verbose_name='زمان آپدیت')
    status = models.CharField(max_length=1 , choices=STATUS_CHOICES ,verbose_name='وضعیت')

    # farsi sazi
    class Meta :
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering=['-publish']


    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = 'زمان انتشار'

    # method for just show published category , and we used in template to doesnot show no published cats
    def category_published(self):
        return self.category.filter(status = True)
    
    # and continue of my manager
    objects = ArtilceManager()