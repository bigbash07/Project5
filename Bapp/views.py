from django.shortcuts import render


def home(request):
	return render(request,"home.html")

def privacy(request):
	return render(request,"privacy.html")

def partner(request):
	return render(request,"partner.html")

def contact(request):	
	return render(request,"contact.html")