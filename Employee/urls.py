from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet

# URLConf
router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]