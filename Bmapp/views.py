from django.shortcuts import render


def information(request):
	return render(request,'information.html')

def hello(request):
	return render(request,'hello.html')

def boom(request):
	return render(request,'boom.html')

def rocket(request):
	return render(request,'rocket.html')
def control(request):
	return render(request,'control.html')