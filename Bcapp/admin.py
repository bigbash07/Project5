from django.contrib import admin
from .models import BcModel

class BcModelAdmin(admin.ModelAdmin):
	search_fields=('full_name',)
	
	list_filter=['blood']

admin.site.register(BcModel,BcModelAdmin)

