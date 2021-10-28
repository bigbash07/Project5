from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError


class BcModel(models.Model):
	full_name = models.CharField(max_length=30 )
	email = models.EmailField()
	phone = models.CharField(max_length=10)
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        )
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES ,default="",blank=True)
	
	
	
	
	aadhaar = models.CharField(default="",max_length=14)
	file = models.FileField(upload_to='uploads',blank=True )
	
	
	age = models.IntegerField(default="")
	Blood_Group = (
	('A' , 'A+'),
	('B' , 'B+'),
	('AB' , 'AB+'),
	('AB' , 'AB-'),
	('O' , 'O'),	
	)
	blood = models.CharField(max_length=2,choices=Blood_Group, default="")
	
	Day = (
	('Mon' ,'1'),
	('Tue' ,'2'),
	('Wed' ,'3'),
	('Thu' ,'4'),
	('Fri' ,'5'),
	('M' ,'6'),
	('o' ,'7'),
	('a' ,'8'),
	('b' ,'9'),
	('c' ,'10'),
	('d' ,'11'),
	('e' ,'12'),
	('f' ,'13'),
	('g' ,'14'),
	('h' ,'15'),
	('i' ,'16'),
	('sa' ,'17'),
	('j' ,'18'),('k' ,'19'),('l' ,'20'),('n' ,'21'),('p' ,'22'),('ao' ,'23'),('adx' ,'24'),('Mas' ,'25'),('sa' ,'26'),('on' ,'27'),('Mn' ,'28'),('asd' ,'29'),('qw' ,'30'),('xl' ,'31'),
	)
	date = models.TextField(max_length=10,choices=Day,default='')
	Month = (
	('J','January'),('F','February'),('M','March'),('A','April'),('M','May'),('Ju','June'),('Jl','July'),('Au','August'),('O','October'),('N','November'),('D','December'),
	)
	month = models.CharField(max_length=10,choices=Month,default="")
	YEAR = (
	('a','2021'),('b','2022'),('c','2023'),('d','2024'),('e','2025'),('f','2026'),('g','2027'),
	)
	year = models.CharField(max_length=4,choices=YEAR,default="")
	
	Health_Issues = (
	('Y' , 'Yes'),
	('N' , 'No'),
	)
	illness = models.CharField(max_length=1, choices=Health_Issues ,default="",blank=True)
	health_issue = models.TextField(max_length=100,default='',blank=True)
	

	
	query = models.TextField(max_length=100,default='',blank=True)
	


	def __str__(self):
		return self.full_name
		
		