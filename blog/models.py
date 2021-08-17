from django.db import models
from django.db.models.fields.related import create_many_to_many_intermediary_model
from django.utils import timezone
from extensions.utils import jalali_converter
# Create your models here.

class Article(models.Model):
    STATUS_CHOICES =(
        # ('d','Draft'),
        # ('p','Published'),
        ('d','پیش نویس'),
        ('p','منتشر شده'),
    )
    title = models.CharField(max_length=255 , verbose_name='عنوان')
    slug = models.SlugField(max_length=100 , verbose_name='اسلاگ')
    descriptions = models.TextField(verbose_name='توضیحات')
    thumbnail = models.ImageField(upload_to='images' , verbose_name='تصویر')
    publish = models.DateTimeField(default=timezone.now , verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True , verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True , verbose_name='زمان آپدیت')
    status = models.CharField(max_length=1 , choices=STATUS_CHOICES ,verbose_name='وضعیت')

    # farsi sazi
    class Meta :
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'


    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = 'زمان انتشار'