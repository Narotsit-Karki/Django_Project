from django.db import models

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
	image = models.TextField()

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

class Blog(models.Model):
	name = models.CharField(max_length = 200)
	date_posted = models.DateField()
	likes = models.IntegerField()
	comments = models.IntegerField()
	title = models.TextField()
	description = models.TextField()
	profile_pic = models.TextField(default = 'img/default.png')
	header_image = models.TextField(default = 'None')

	def __str__(self):
		return f"< {self.name} : {self.date_posted} >"

