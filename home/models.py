from django.db import models
from ckeditor.fields import RichTextField
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

class User(models.Model):
	fname = models.CharField(max_length = 400)
	lname = models.CharField(max_length = 400)
	slug = models.CharField(max_length = 80,unique = True)
	email = models.EmailField(unique = True, max_length = 600)
	password = models.CharField(max_length = 15)
	profile_pic = models.ImageField(default = 'img/default.png',blank = True)

	def __str__(self):
		return f"< {self.email} >"


class Comment(models.Model):
	slug = models.CharField(max_length = 40,unique = True)
	comment_text = models.TextField()
	comment_user = models.ForeignKey(User,on_delete = models.CASCADE)
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
	likes = models.IntegerField()
	title = models.TextField()
	content = RichTextField(blank=True,null=True)
	header_image = models.ImageField()
	blog_user = models.ForeignKey(User,on_delete = models.CASCADE)
	comments = models.ForeignKey(Comment,on_delete = models.CASCADE,blank = True , null = True)
	category = models.ManyToManyField(Post_Categories)
	def __str__(self):
		return f"< {self.title} : {self.date_posted} >"



