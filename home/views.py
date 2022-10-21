from django.shortcuts import render , redirect
import os ,shutil
# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin


from .models import *
from django.views.generic import View
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator
countries = []
with open('home/countries.txt','r') as country:
	read = country.readline()
	while read:
		countries.append(read.strip('\n'))
		read = country.readline()

class BaseView(View):
	login_url = 'accounts/login'
	views = {}
	views['feedbacks'] = FeedBack.objects.all()
	views['Services'] = Service.objects.all()
	views['Blogs'] = Blog.objects.all()
	price_plans = Price_Plan.objects.all()
	views['Categories'] = Categories =  Post_Categories.objects.all()
	views['Popular'] =  Blog.objects.all().order_by("-likes")[:3]
	views['Popular_Single_Blog'] = views['Popular'][0]

	for p in price_plans:
		views[p.plan_name] = p.price



def signup(request):
	if request.method  == 'POST':
		username = request.POST['uname']
		if not User.objects.filter(username = username).exists():
			email = request.POST['email']
			if not User.objects.filter(email = email).exists():
				password = request.POST['password']
				confirm_password = request.POST['c_password']
				if password == confirm_password:
					new_user = User.objects.create_user(
						username = username,
						email = email,
						password = password

						)
					# creating a new directory to store users pictures
					try:
						os.mkdir(f'media/{username}')
					except:
						pass
					shutil.copyfile('media/default.png',f'media/{username}/default.png')

					new_user.save()
					messages.success(request,'Signed up Successfully ')
					return redirect("accounts/login")
				else:
					# same password and confirm password error message
					messages.error(request,'Enter Same Password on Both Fields')
					return redirect(signup)
			else:
				# email exists error message
				messages.error(request,f'Email {email} already exists')
				return redirect(signup)


		else:
			# username already taken message
			messages.error(request,f'Username {username} Already exits')
			return redirect(signup)




	return render(request,'signup.html')

class HomeView(BaseView):
	def get(self,request):
		self.views
		self.views['Title'] = 'Home'
		return render(request,'index.html',self.views)


def about(request):
	# views = base()
	views = {}
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
	# views = Base()
	views = {}
	return render(request,'portfolio.html',views)

def price(request):
	# views = index_base()
	views = {}
	return render(request,'price.html',views)

def services(request):
	# views = index_base()
	views = {}
	return render(request,'services.html',views)



class Elements(BaseView):

	def get(self,request):
		return render(request,'elements.html')


class ProfileView(LoginRequiredMixin,BaseView):
	login_required = True
	def get(self,request):
		self.views
		self.views['Title'] = f'Profile: {request.user.username}'
		self.views['Countries'] = countries
		self.views['Blogs'] = Blog.objects.filter(user = request.user)

		return render(request, 'account-profile.html', self.views)

	def update_profile_pic(self,profile_pic_url):
		random_hex = os.urandom(10).hex()
		f_name, f_ext = os.path.splitext(profile_pic_url)
		new_picture_file = random_hex + f_ext
		picture_path = os.path.join('home', 'media/profile_pics', new_picture_file)
		output_size = (400, 400)
		i = Image.open(profile_pic_url)
		i.thumbnail(output_size)
		i.save(picture_path)
		return new_picture_file

	def post(self,request):
		if request.method == 'POST':
			fname = request.POST['fname']
			lname = request.POST['lname']
			email = request.POST['email']
			phone = request.POST['phone']
			address = request.POST['address']
			country = request.POST['country']
			profile_pic = request.FILES['image']

			request.user.first_name = fname
			request.user.last_name = lname
			request.user.email = email
			request.user.phone = phone
			request.user.user_info.address = address
			request.user.user_info.country = country
			request.user.user_info.address = address
			request.user.save()
			messages.success(request,'Successfully Updated your profile')
			return redirect('/profile')


# class CategoryView(View):
# 	def get(self,request,category):
# 		self.views = self.get_views(request,category)

# 		return render(request,'blog-home.html',self.views)
# 	def get_views(self,request,category):
# 		self.views = base()
# 		self.category = Post_Categories.objects.get(name = category)
# 		self.Blogs = self.category.blogs.all()

# 		self.views['Popular'] = Blog.objects.all().order_by("-likes")[:3]
# 		self.pages = Paginator(self.Blogs,4)
# 		self.views['Pages'] = self.pages
# 		self.page_number = request.GET.get('page')
# 		self.views['Blogs'] = self.pages.get_page(self.page_number)
# 		return self.views


class Blog_Home(BaseView):
	def get(self,request):
		self.views
		blogs = Blog.objects.all().order_by('-date_posted')
		pages = Paginator(blogs,4)
		self.views['Pages'] = pages
		page_number = request.GET.get('page')
		self.views['Blogs'] = pages.get_page(page_number)

		return render(request,'blog-home.html',self.views)

class Blog_Single(BaseView):
	def get(self,request,slug):
		self.views
		self.views['single_blog'] = Blog.objects.get(slug = slug)

		return render(request,'blog-single.html',self.views)


# def login_valid(request):

# 	if request.method == 'POST':
# 		email = request.POST['u_email']
# 		password = request.POST['u_password']

# 		try:
# 			user = User.objects.get(email = email)
# 		except:
# 			user = None

# 		if user:
# 			if check_password(password,user.password):
# 				messages.success(request , f" Welcome, {user.fname} {user.lname}")
# 				return redirect(home)
# 			else:
# 				messages.warning(request, 'Invalid Password')
# 				return redirect(login)
# 		else:
# 			messages.warning(request, 'Email Doesnot Exist , Sign up for one')
# 			return redirect(signup)




# 	elif request.method == 'GET':
# 		raise PermissionDenied

# 	messages.info(request,'Login Successfull ')
# 	return redirect(home)


# def signup_valid(request):
# 	if request.method == 'POST':
# 		fname = request.POST['fname']
# 		lname = request.POST['lname']
# 		email = request.POST['email']
# 		user_password = request.POST['password']
# 		confirm_password = request.POST['confirmpassword']
# 		if user_password == confirm_password:
# 			hashed_user_pass = make_password(user_password)
# 			user_data = User.objects.create(fname = fname , slug = os.urandom(3).hex() ,lname = lname ,email = email,password = hashed_user_pass)
# 			user_data.save()
# 			messages.success(request,f'Signed Up Successfully. Welcome , {fname} {lname}')
# 			return redirect(home)
# 		else:
# 			messages.warning(request,'Enter same Password on Both Fields !')
# 			return redirect(signup)
# 	elif request.method == 'GET':
# 		raise PermissionDenied

# 	return redirect(home)

# -----------------------API VIEWS -----------------------#
# from .serializers import *
# from rest_framework import viewsets
# # ViewSets define the view behavior.
# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = ProductSerializer
