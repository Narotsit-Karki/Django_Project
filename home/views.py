from django.shortcuts import render
# Create your views here.
from .models import *
def index_base():
	views = {}
	views['feedbacks'] = FeedBack.objects.all()
	views['Services'] = Service.objects.all()
	return views


def price_plan_base():
	views = {}
	price_plans = Price_Plan.objects.all()
	for p in price_plans:
		views[p.plan_name] = p.price
	return views




def home(request): #request is
	views = index_base()
	return render(request,'index.html',views)


def about(request):
	views = index_base()
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
	price = price_plan_base()
	return render(request,'price.html',price)

def services(request):
	views = index_base()
	return render(request,'services.html',views)
	
