from django.db import models

# Create your models here.

class Livros(models.Model):

    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    editora = models.CharField(max_length=255)
    numeroPaginas = models.CharField(max_length=255)
    idioma = models.CharField(max_length=255)
    descricao = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
