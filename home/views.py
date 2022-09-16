from django.shortcuts import render

# Create your views here.

def home(request): #request is 
	return render(request,'index.html')


def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')

def portfolio(request):
	return render(request,'portfolio.html')

def price(request):
	return render(request,'price.html')

def services(request):
	return render(request,'services.html')
	