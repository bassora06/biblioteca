from django.db import models

# Create your models here.

class Livros(models.Model):

    IDIOMAS = [
        ('Português' , 'Português'),
        ('Inglês' , 'Inglês'),
        ('Italiano' , 'Italiano'),
        ('Francês' , 'Francês'),
        ('Espanhol' , 'Espanhol'),
        ('Alemão' , 'Alemão')
    ]

    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    editora = models.CharField(max_length=255)
    numeroPaginas = models.CharField(max_length=255)
    idioma = models.CharField(max_length=9, choices=IDIOMAS)
    descricao = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
