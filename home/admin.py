from django.contrib import admin
from .models import *
# registering the models here
# to add Contact form in the admin
admin.site.register(Contact)
admin.site.register(FeedBack)
# admin.site.register(Price_Plan)
admin.site.register(Service)
admin.site.register(Blog)
# for showing table in the admin panel
from django.utils.html import format_html

class BlogUser(admin.ModelAdmin):
	def image_tag(self,obj):
		return format_html(f"<img src = '{obj.profile_pic.url}' class = 'avatar' style= 'object-fit: cover;vertical-align: middle;width: 50px;height: 50px;border-radius: 50%;'/>" )

	image_tag.short_description = 'Profile Pic'


	list_display = ('image_tag','user')


admin.site.register(User_Info,BlogUser)
admin.site.register(Comment)
admin.site.register(Post_Categories)