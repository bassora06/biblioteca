# importações 
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse            #  requisição
from .forms import BookForm                     #  form de livros
from django.contrib import messages             # mensagens para exibição do usuáio
from django.core.paginator import Paginator     #  classe de paginação do django
from .models import Livros


# lista todos os livros no front end
def listBook(request):

    search = request.GET.get('search')  # o search passado com parametro do método get é o name do input de busca

    if search:

        livros_search = Livros.objects.filter(titulo__icontains=search)

        paginator = Paginator(livros_search, 5)
    
    else:

        livros_list = Livros.objects.all().order_by('titulo') # pega todos os objetos da tabela livros do banco

        paginator = Paginator(livros_list, 5) # recebe variavel de lista de livros e quantidade

    page = request.GET.get('page') # variavel recebe a requesção da página por get

    livros = paginator.get_page(page) # a paginação pega o dado da página e coloca na variavel livros

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
