from django.urls import path
from . import views

urlpatterns = [
    path('adminHome/', views.adminHome, name="adminHome"),

]