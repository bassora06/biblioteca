from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('cadastro/', views.SignUp.as_view(), name='signup'),
   
]
