from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import BookForm
from django.contrib import messages
from .models import Livros

# Create your views here.


# lista todos os livros no front end
def listBook(request):
    livros = Livros.objects.all() # pega todos os objetos da tabela livros do banco
    return render(request, 'livros/list.html', {'livros' : livros})


# cria novo livro
def newBook(request): 
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(request, 'Livro adicionado com sucesso')
            return redirect('/')

    else:
        form = BookForm()
        return render(request, 'livros/newBook.html', {'form': form})
    

# edita o livro
def editBook(request, id):
    livro = get_object_or_404(Livros, pk=id)
    form = BookForm(instance=livro) # instance pega os dados que do livro que já existem e pré copula no formulário

    if request.method == 'POST':
        form = BookForm(request.POST, instance=livro)

        if form.is_valid():
            livro.save()
            messages.info(request, 'Livro editado com sucesso')
            return redirect('/')
        else:
            return render(request, 'livros/editBook.html', {'form': form, 'livro': livro})
    else:
        return render(request, 'livros/editBook.html', {'form': form, 'livro': livro})
    

# deleta o livro
def deleteBook(request, id):
    livro = get_object_or_404(Livros, pk=id)
    livro.delete()
    messages.info(request, 'Livro deletado com sucesso')
    return redirect('/')

def viewBook(request, id):
    livro = get_object_or_404(Livros, pk=id)
    return render(request, 'livros/book.html', {'livro' : livro})
