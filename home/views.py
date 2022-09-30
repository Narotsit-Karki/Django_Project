from django.shortcuts import render , redirect
import os
# Create your views here.
from .models import *
from django.views.generic import View
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator

def base():
	views = {}
	views['feedbacks'] = FeedBack.objects.all()
	views['Services'] = Service.objects.all()
	views['Blogs'] = Blog.objects.all()
	price_plans = Price_Plan.objects.all()
	views['Categories'] = Categories =  Post_Categories.objects.all()
	views['Popular'] =  Blog.objects.all().order_by("-likes")[:3]
	for p in price_plans:
		views[p.plan_name] = p.price
	return views



def price_plan_base():
	views = {}




def login(request):
	return render(request,'login.html')


def signup(request):
	return render(request,'signup.html')

def home(request): #request is
	
	views = base()
	return render(request,'index.html',views)


def about(request):
	views = base()
	return render(request,'about.html',views)

def contact(request):
	if request.method == "POST":
		name = request.POST['name']
		email_address = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
		# creating the object to save
		data = Contact.objects.create( name = name , 
									   email_address = email_address , 
									   subject = subject , 
									   message = message
									   )

		data.save() #svaing the database
	return render(request,'contact.html')

def portfolio(request):
	return render(request,'portfolio.html')

def price(request):
	views = index_base()

	return render(request,'price.html',views)

def services(request):
	views = index_base()
	return render(request,'services.html',views)
	


class Elements(View):

	def get(self,request):
		return render(request,'elements.html')



class CategoryView(View):
	def get(self,request,category):
		self.views = self.get_views(request,category)

		return render(request,'blog-home.html',self.views)
	def get_views(self,request,category):
		self.views = base()
		self.category = Post_Categories.objects.get(name = category)
		self.Blogs = self.category.blogs.all()
		
		self.views['Popular'] = Blog.objects.all().order_by("-likes")[:3]
		self.pages = Paginator(self.Blogs,4)
		self.views['Pages'] = self.pages
		self.page_number = request.GET.get('page')
		self.views['Blogs'] = self.pages.get_page(self.page_number)
		return self.views
	



def blog_home(request):
	views = base()
	blogs = Blog.objects.all().order_by('-date_posted')
	pages = Paginator(blogs,4)
	views['Pages'] = pages
	page_number = request.GET.get('page')
	views['Blogs'] = pages.get_page(page_number)
	return render(request,'blog-home.html',views)

def blog_single(request):
	views = base()
	views['single_blog'] = Blog.objects.get(slug = 'b05')
	return render(request,'blog-single.html',views) 


def login_valid(request):

	if request.method == 'POST':
		email = request.POST['u_email']
		password = request.POST['u_password']

		try:
			user = User.objects.get(email = email)
		except:
			user = None

		if user:
			if check_password(password,user.password):
				messages.success(request , f" Welcome, {user.fname} {user.lname}")
				return redirect(home)
			else:
				messages.warning(request, 'Invalid Password')
				return redirect(login)
		else:
			messages.warning(request, 'Email Doesnot Exist , Sign up for one')
			return redirect(signup)




	elif request.method == 'GET':
		raise PermissionDenied

	messages.info(request,'Login Successfull ')
	return redirect(home)


def signup_valid(request):
	if request.method == 'POST':
		fname = request.POST['fname']
		lname = request.POST['lname']
		email = request.POST['email']
		user_password = request.POST['password']
		confirm_password = request.POST['confirmpassword']
		if user_password == confirm_password:
			hashed_user_pass = make_password(user_password)
			user_data = User.objects.create(fname = fname ,lname = lname , email = email,password = hashed_user_pass)
			user_data.save()
			messages.success(request,f'Signed Up Successfully. Welcome , {fname} {lname}')
			return redirect(home)
		else:
			messages.warning(request,'Enter same Password on Both Fields !')
			return redirect(signup)
	elif request.method == 'GET':
		raise PermissionDenied

	return redirect(home)