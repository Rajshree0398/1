from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=245,unique=True)
	mobile = models.CharField(max_length=12,unique=True)
	
	#mobile_no = models.PhoneNumberField(null=False, blank=False, unique=True)

	def __str__(self):
		return self.email

class Customer(models.Model):
	#user = models.OneToOneField(
		#User,
		#on_delete=models.CASCADE,
		#primary_key=True,)
	first_name = models.CharField(max_length=100)

	profile_no = models.CharField(max_length=100)
	user =  models.ForeignKey(User, on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.profile_no





