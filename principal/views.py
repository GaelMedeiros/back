from django.shortcuts import render

# Create your views here.
def findex(request):
    return render(request, "index.html")