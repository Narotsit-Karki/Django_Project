
from .views import *
from django.urls import path

# registering urls 
urlpatterns = [
   path('',home , name = "home"), # then register this url again in the urls.py of blog 
   # path('path',function from views, name)
   path('about',about,name ="about-us"),
   path('contact',contact,name ="contact"), #name is used to redirect from this page to some other page
   path('portfolio',portfolio,name ="portfolio"),
   path('price',price,name ="price"),
   path('services',services,name ="services")
   ]


