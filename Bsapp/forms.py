from django import forms
from .models import BsModel

class BsForm(forms.ModelForm):
	
	class Meta:
		model = BsModel
		fields = [
			'name'
			
		]