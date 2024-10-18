"""
URL configuration for biblioteca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listBook, name='list-book'),
    path('book/<int:id>', views.viewBook, name='view-book'),
    path('newBook/', views.newBook, name='new-book'),
    path('editBook/<int:id>', views.editBook, name='edit-book'),
    path('deleteBook/<int:id>', views.deleteBook, name='delete-book'),
]
