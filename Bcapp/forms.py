from django import forms
from .models import BcModel



class BcForm(forms.ModelForm):
	
	class Meta:
		model = BcModel
		fields = [
			'full_name',
			'email',
			'phone',
			'gender',
			'age',
			'blood',
			'illness', 
			'health_issue',
			'date',
			'month',
			'year',
			'file',
			'aadhaar',
			
			'query'
		]




		widgets = {
			'full_name': forms.TextInput(attrs={"class":"input", "placeholder":"Your name"}),
			'email': forms.EmailInput(attrs={"class":"input", "placeholder":"Your email"}),
			'phone': forms.TextInput(attrs={"class":"input", "placeholder":"Your No. pls"}),
			'aadhaar': forms.TextInput(attrs={"class":"input", "placeholder":"Enter Your aadhaar no"}),
			'health_issue': forms.Textarea(attrs={"class":"input", "placeholder":"If any previous health issues, Please specify"}),
			'query': forms.Textarea(attrs={"class":"input", "placeholder":"Any Doubt?"})
		}
		

