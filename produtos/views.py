from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Produto
from django.db.models import Q

def pesquisa_produto(request):
    query = request.GET.get('q', '')
    query_words = query.split()
    search_query = Q()

    for word in query_words:
        search_query &= (Q(descricao__icontains=word) | Q(codigo_do_produto__icontains=word))
    
    produtos = Produto.objects.filter(search_query)
    return render(request, 'produtos/pesquisa.html', {'produtos': produtos, 'query': query})

def produto_update(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        codigo = request.POST.get('codigo')
        descricao = request.POST.get('descricao')
        venda = request.POST.get('venda', None)
        revenda = request.POST.get('revenda', None)
        atacado = request.POST.get('atacado', None)

        if not produto_id:
            messages.error(request, 'ID do produto não fornecido.')
            return redirect('pesquisa_produto') # Corrigido para usar o nome da URL
        
        produto = get_object_or_404(Produto, pk=produto_id)
        produto.codigo_do_produto = codigo
        produto.descricao = descricao

        # Atualiza os campos se forem fornecidos
        if venda is not None:
            produto.venda = venda
        if revenda is not None:
            produto.revenda = revenda
        if atacado is not None:
            produto.atacado = atacado

        produto.save()

        messages.success(request, 'Produto atualizado com sucesso.')
        return redirect('pesquisa_produto') # Corrigido para usar o nome da URL
