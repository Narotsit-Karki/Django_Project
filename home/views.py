from django.shortcuts import render

# Create your views here.

def home(request): #request is 
	return render(request,'index.html')


