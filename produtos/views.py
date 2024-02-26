from django.shortcuts import render
from .models import Produto

def pesquisa_produto(request):
    query = request.GET.get('q', '')  # Obtém o parâmetro de pesquisa da URL
    produtos = Produto.objects.all()
    if query:  # Se o parâmetro 'q' não estiver vazio, filtra os produtos
        produtos = produtos.filter(codigo_do_produto__icontains=query) | produtos.filter(descricao__icontains=query)
    return render(request, 'produtos/pesquisa.html', {'produtos': produtos, 'query': query})
