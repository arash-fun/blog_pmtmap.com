from django.urls import path
from .views import detail_article, home 




app_name = "blog"

urlpatterns = [
    path ('', home , name='home'),
    path ('article/<slug:slug>' ,detail_article , name ='detail_article'),

]
