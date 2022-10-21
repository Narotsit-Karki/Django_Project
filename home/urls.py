
from .views import *
from django.urls import path

# # registering urls
urlpatterns = [
   path('',HomeView.as_view(), name = "home"), # then register this url again in the urls.py of blog
   # path('path',function from views, name)
   path('about',about,name ="about-us"),
   path('contact',contact,name ="contact"), #name is used to redirect from this page to some other page
   path('portfolio',portfolio,name ="portfolio"),
   path('price',price,name ="price"),
   path('services',services,name ="services"),
   path('elements',Elements.as_view(),name = "elements"),
   path('blog-home',Blog_Home.as_view(),name="blog-home"),
   path('blog-single/<slug>',Blog_Single.as_view(),name="blog-single"),
   path('signup',signup,  name ='home-signup'),
   path('profile',ProfileView.as_view() , name = 'user-profile'),
   # path('blog-home/<category>',CategoryView.as_view(),name = 'blog-home-category'),
   ]
#
#
