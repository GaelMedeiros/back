from django.shortcuts import render
from .models import Cliente
# Create your views here.

def fcliente(request):
    clientes = Cliente.objects.all()
    return render(request, "rel_cliente.html", {"clientes":clientes})

def Fcadcliente(request):
    return render(request, "cad_cliente.html")

def salvar(request):
    return render(request, "rel_cliente;html")
    vnome = request.POST.get("nome")
    vtelefone = request.POST.get("telefone")
    vemail = request.POST.get("email")
    if vnome:
        Produto.objects.create(nome=vnome, telefone=vtelefone, email=vemail)
        return redirect(fcliente)

def exibir(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, "update.html", {"clientes": cliente})

def excluir(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect(fcliente)

def update(request, id):
    vnome = request.POST.get("nome")
    vtelefone = request.POST.get("telefone")
    vemail = request.POST.get("email")
    cliente = Cliente.objects.get(id=id)
    cliente.nome = vnome
    cliente.telefone = vtelefone
    cliente.email = vemail
    cliente.save()
    return redirect(fcliente)