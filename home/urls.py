
from .views import *
from django.urls import path

# registering urls 
urlpatterns = [
   path('',home , name = "home") # then register this url again in the urls.py of blog 
   # path('path',function from views, name)
]

