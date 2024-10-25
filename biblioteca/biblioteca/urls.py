from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('livros.urls')),
    path('contas/', include('contas.urls')),
    path('contas/', include('django.contrib.auth.urls')),
]
