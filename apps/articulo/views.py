from django.shortcuts import render
from .models import Articulo
from django.views.generic import ListView

#Todos los artículos
class ArticuloListView(ListView):
    model = Articulo
    template_name = "articulo/articulos.html" 
    context_object_name = "articulos" 

    def get_queryset(self):
        queryset = super().get_queryset()
        orden = self.request.GET.get('orden')
        if orden == 'reciente':
            queryset = queryset.order_by('-fecha_publicacion')
        elif orden == 'antiguo':
            queryset = queryset.order_by('fecha_publicacion')
        elif orden == 'alfabetico':
            queryset = queryset.order_by('titulo')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orden'] = self.request.GET.get('orden', 'reciente')
        return context

