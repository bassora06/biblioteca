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
