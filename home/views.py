from django.shortcuts import render
# Create your views here.
from .models import *
def home(request): #request is

	if request.method == 'GET':


	return render(request,'index.html')


def about(request):
	return render(request,'about.html')

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
	return render(request,'price.html')

def services(request):
	return render(request,'services.html')
	
