from django import forms

from .models import Livros


class BookForm(forms.ModelForm):

    class Meta():
        model = Livros
        fields = ('titulo', 'autor', 'editora', 'numeroPaginas', 'idioma', 'descricao')