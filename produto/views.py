from django.shortcuts import render, redirect
from .models import Produto


# Create your views here.
def fproduto(request):
    produtos = Produto.objects.all()
    return render(request, "rel_produto.html", {"produtos":produtos})

def salvar(request):
    vnome = request.POST.get("nome")
    vdescricao = request.POST.get("descricao")
    vpreco = request.POST.get("preco")
    vquantidade = request.POST.get("quantidade")
    if vnome:
        Produto.objects.create(nome=vnome, descricao=vdescricao, preco=vpreco, quantidade=vquantidade)
        return redirect(fproduto)


def exibir(request, id):
    produto = Produto.objects.get(id=id)
    return render(request, "update.html", {"produtos": produto})



def excluir(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect(fproduto)

def update(request, id):
    vnome = request.POST.get("nome")
    vdescricao = request.POST.get("descricao")
    vpreco = request.POST.get("preco")
    vquantidade = request.POST.get("quantidade")
    produto = Produto.objects.get(id=id)
    produto.nome = vnome
    produto.descricao = vdescricao
    produto.preco = vpreco
    produto.quantidade = vquantidade
    produto.save()
    return redirect(fproduto)