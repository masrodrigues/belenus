from django.shortcuts import render
from .models import Produto

from django.db.models import Q

def pesquisa_produto(request):
    query = request.GET.get('q', '')

    # Divide a string de consulta em palavras
    query_words = query.split()

    # Cria uma query que procura cada palavra em qualquer parte dos campos desejados
    search_query = Q()
    for word in query_words:
        search_query &= (
            Q(descricao__icontains=word) | 
            Q(codigo_do_produto__icontains=word)
        )
    
    # Filtra os produtos com a query construída
    produtos = Produto.objects.filter(search_query)

    return render(request, 'produtos/pesquisa.html', {'produtos': produtos, 'query': query})

