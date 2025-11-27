from django.urls import path
from .views import *

app_name = 'apps.articulo'

urlpatterns = [
    path('articulos/', ArticuloListView.as_view(), name='articulos'),#todos los artículos
]
