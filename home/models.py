from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import mark_safe
from django.contrib.auth.models import User
# Create your mode
# make migrations after every update
	# python manage.py make migrations
	# python manage.oy migrate
	# then register in admin.py

class Contact(models.Model):
	name = models.CharField(max_length = 400)
	email_address = models.EmailField(max_length = 300)
	subject = models.TextField()
	message = models.TextField()


	def __str__(self):  # to represent name in the admin panel field
		return self.email_address


class FeedBack(models.Model):
	name = models.CharField(max_length = 400)
	post = models.CharField(max_length = 500)
	comment = models.TextField()
	image = models.ImageField()

	def __str__(self):
		return self.name



class Price_Plan(models.Model):
	plan_name = models.CharField(max_length = 300)
	price = models.FloatField()

	def __str__(self):
		return self.plan_name

class Service(models.Model):
	name = models.CharField(max_length = 400)
	icon = models.CharField(max_length = 100)
	description = models.TextField()

	def __str__(self):
		return self.name

class User_Info(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	profile_pic = models.ImageField(default = 'default.png',blank = True)
	date_of_birth = models.DateField(default = None)
	job = models.TextField(blank = True)
	phone = models.IntegerField(blank = True)
	country = models.CharField(max_length = 30,blank = True)
	address = models.CharField(max_length = 400 ,blank = True)



class Comment(models.Model):
	slug = models.CharField(max_length = 40,unique = True)
	comment_text = models.TextField()
	comment_user = models.OneToOneField(User_Info,on_delete = models.CASCADE)
	date_posted = models.DateField()
	likes = models.IntegerField()


	def __str__(self):
		return f"< {self.comment_user} : {self.date_posted} >"


class Post_Categories(models.Model):
	slug = models.CharField(unique = True,max_length = 40)
	name = models.CharField(max_length = 400)
	blogs = models.ManyToManyField('Blog')

	def __str__(self):
		return f" < {self.name} >"

class Blog(models.Model):
	slug = models.CharField(max_length = 50,unique = True)
	date_posted = models.DateField()
	title = models.TextField()
	content = RichTextField(blank=True,null=True)
	header_image = models.ImageField()
	user = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
	category = models.ManyToManyField(Post_Categories, null = True)
	comments = models.ManyToManyField(Comment , null = True)
	likes = models.IntegerField(blank = True)
	def __str__(self):
		return f"< {self.title} : {self.date_posted} >"



