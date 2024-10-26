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

    titulo = models.CharField(max_length=255, blank=False)
    autor = models.CharField(max_length=255, blank=False)
    editora = models.CharField(max_length=255, blank=False)
    numeroPaginas = models.PositiveIntegerField(max_length=255, blank=False)
    idioma = models.CharField(max_length=9, choices=IDIOMAS, default='Português')
    descricao = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



