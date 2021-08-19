from django.urls import path
from .views import detail_article, home ,category 




app_name = "blog"

urlpatterns = [
    path ('', home , name='home'),
    path ('page/<int:page>', home , name='home'),
    path ('article/<slug:slug>' ,detail_article , name ='detail_article'),
    path ('category/<slug:slug>' ,category , name='category'),
    path ('category/<slug:slug>/page/<int:page>', category , name='category'),

]
