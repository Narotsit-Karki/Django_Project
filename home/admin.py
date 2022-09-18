from django.contrib import admin
from .models import *
# registering the models here
# to add Contact form in the admin
admin.site.register(Contact)
admin.site.register(FeedBack)