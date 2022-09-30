
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
   path('services',services,name ="services"),
   path('elements',Elements.as_view(),name = "elements"),
   path('blog-home',blog_home,name="blog-home"),
   path('blog-single',blog_single,name="blog-single"),
   path('login/',login , name = 'home-login'),
   path('signup/',signup ,  name ='home-signup'),
   path('login/login-valid',login_valid,name = 'home-login-valid'),
    path('signup/signup-valid',signup_valid,name = 'home-signup-valid'),
   path('blog-home/<category>',CategoryView.as_view(),name = 'blog-home-category'),
   ]


