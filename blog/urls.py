from django.http.response import HttpResponseNotAllowed
from django.urls import path
from django.http import HttpResponse
from .views import home 




app_name = 'blog'

urlpatterns = [
    path ('', home , name='home'),

]
