from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from random import randrange
from Blood_Do_Camp.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from .forms import BcForm
from .models import BcModel


def user_signup(request):
	if request.method =="POST":
		un  = request.POST.get("un")
		em =  request.POST.get("em")
		try:
			usr = User.objects.get(username=un)
			return render (request,"user_signup.html" ,{"msg":"user exists "})
		except User.DoesNotExist:
			try:
				usr = User.objects.get(email=em)
				return render(request,"user_signup.html",{"msg":"email exists"})
			except User.DoesNotExist:  
				text = "0123456789abcdefghijklmnopqrstuvwxyz"
				pw = ""
				for i in range(8):
					pw = pw + text[randrange(len(text))]
				send_mail("welcome" , " Your Password is " + str(pw) , EMAIL_HOST_USER, [em])
				usr = User.objects.create_user(username=un , password=pw , email=em)
				usr.save()
				return redirect("user_login")
	else:
		return render(request,"user_signup.html")

def user_login(request):
	if request.method == "POST":
		un = request.POST.get("un")
		pw = request.POST.get("pw")
		usr = authenticate(username=un,password=pw)
		if usr is None:
			return render(request,"user_login.html",{"msg":"Invalid Login"})
		else:
			login(request,usr)
			return redirect("home")
	else:
		return render(request,"user_login.html")
def user_resetpassword(request):
	if request.method == "POST":
		un = request.POST.get("un")
		em = request.POST.get("em")
		try:
			usr = User.objects.get(username=un) and User.objects.get(email=em)
		
			text = "0123456789abcdefghijklmnopqrstuvwxyz"
			pw = ""
			for i in range(8):
				pw = pw + text[randrange(len(text))]	
				send_mail("New Password" , " Your New Password is " + str(pw) , EMAIL_HOST_USER, [em])
				usr.set_password(pw)
				usr.save()
				return redirect("user_login")
		except User.DoesNotExist:
			return render(request,"user_resetpassword.html",{"msg":"Invalid Details Pls check"})
	else:

		return render(request,"user_resetpassword.html")

def user_logout(request):
	logout(request)
	return render(request,"user_login.html")

def user_personal_details(request):
	
	if request.method == "POST":
		fn = request.POST.get("full_name")
		
		em = request.POST.get("email")
		ph = int(request.POST.get("phone"))
		gen = request.POST.get("gender")
		que = request.POST.get("query")
		adn = request.POST.get("aadhaar")
		hi = request.POST.get("health_issue")
		ill = request.POST.get("illness")
		fl = request.POST.get("file")
		ag = request.POST.get("age")
		da = request.POST.get("date")
		blo = request.POST.get("blood")
		mo = request.POST.get("month")
		ye = request.POST.get("year")
		if BcModel.objects.filter(aadhaar=adn).exists():
			return render(request,"user_personal_details.html",{"msg":"Pls check Your addhar"})
		elif BcModel.objects.filter(email=em).exists():
			return render(request,"user_personal_details.html",{"msg":"Pls check Your Email"})
			
		
		else:
			data = BcForm(request.POST,request.FILES)
			d = BcModel(full_name=fn,email=em,phone=ph,gender=gen,query=que,health_issue=hi,illness=ill,file=fl,aadhaar =adn,age=ag,date=da,blood=blo,month=mo,year=ye)
		
			d.save()
			fm = BcForm()
			return render(request,"user_personal_details.html",{"msg":"Thank You for  Registering with us will get back to you as soon as possible"})
		
	
		
	else:
		fm = BcForm()
		return render(request,"user_personal_details.html",{"fm":fm},)


			
				
