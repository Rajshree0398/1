from rest_framework import serializers

from app1.models import User, Customer

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('first_name','last_name','email','mobile')

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = ('first_name','profile_no')