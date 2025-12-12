from django.shortcuts import render
from apps.articulo.models import Categoria, Articulo

#def index(request):
#    articulos = Articulo.objects.all()[:3]  # por ejemplo, los 3 primeros
#    return render(request, "index.html", {"articulos": articulos})


def index(request):
    articulos = Articulo.objects.all()[:3]

    # nombres y assets para las 3 slides:
    wanted = [
        {'name': 'Últimas Noticias', 'img': 'img/carrusel1.jpg', 'desc': 'Todo lo que necesitás saber hoy.'},
        {'name': 'Actualidad',       'img': 'img/carrusel2.jpg', 'desc': 'Información precisa y clara.'},
        {'name': 'Opiniones',        'img': 'img/carrusel3.jpg', 'desc': 'Los análisis más relevantes.'},
    ]

    # buscamos las categorías en la DB
    categorias = Categoria.objects.filter(nombre__in=[w['name'] for w in wanted])
    cat_map = {c.nombre: c for c in categorias}

    slides = []
    for w in wanted:
        cat = cat_map.get(w['name']) 
        slides.append({
            'categoria': cat,
            'img': w['img'],
            'desc': w['desc'],
            'title': w['name']
        })

    return render(request, "index.html", {
        "articulos": articulos,
        "slides": slides
    })


def nosotros(request):
    return render(request, "nosotros/nosotros.html")

# Pag no encontrada
def error_404(request, exception):
    return render(request, '404.html', status=404)