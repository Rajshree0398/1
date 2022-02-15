from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from app1.serializers import UserSerializer, CustomerSerializer
from app1.models import User, Customer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class CustomerViewSet(viewsets.ModelViewSet):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer