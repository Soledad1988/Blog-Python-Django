from django.shortcuts import render
from apps.articulo.models import Articulo   # IMPORTANTE

def index(request):
    articulos = Articulo.objects.all()[:3]  # por ejemplo, los 3 primeros
    return render(request, "index.html", {"articulos": articulos})

def nosotros(request):
    return render(request, "nosotros/nosotros.html")