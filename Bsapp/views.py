from django.shortcuts import render
from .forms import BsForm
from .models import BsModel

def appointment(request):
	
	if request.method == "POST":
		na = request.POST.get("name")
		
		datat = BsForm(request.POST)
		da = BsModel(name=na)
		da.save()
		form = BsForm()
		return render(request,"appointment.html")
	
	else:
	
		form = BsForm()
		return render(request,'appointment.html')
	