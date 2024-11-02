from django.shortcuts import render

# Create your views here.
def fproduto(request):
    return render(request, "cad_produto.html")