from django.urls import include, path
from rest_framework import routers
from app1.views import UserViewSet, CustomerViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'customer', CustomerViewSet)

urlpatterns = [
   path('', include(router.urls)),
]