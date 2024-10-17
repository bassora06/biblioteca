from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import BookForm
from django.contrib import messages
from .models import Livros

# Create your views here.

def helloworld(request):
    return HttpResponse('Hello world')


def listaLivros(request):
    livros = Livros.objects.all()
    return render(request, 'livros/list.html', {'livros' : livros})


def newBook(request): 
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            livro = form.save(commit=False)
            livro.save()
            messages.info(request, 'Livro adicionado com sucesso')
            return redirect('/')

    else:
        form = BookForm()
        return render(request, 'livros/newBook.html', {'form': form})
    

def deleteBook(request, id):
    livro = get_object_or_404(Livros, pk=id)
    livro.delete()
    messages.info(request, 'Livro deletado com sucesso')
    return redirect('/')

def editBook(request, id):
    livro = get_object_or_404(Livros, pk=id)
    form = BookForm(instance=livro)

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
    
def deleteBook(request, id):
    livro = get_object_or_404(Livros, pk=id)
    livro.delete()
    messages.info(request, 'Livro deletado com sucesso')
    return redirect('/')
