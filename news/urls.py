from django.urls import path
from .views import *

app_name = 'news'

urlpatterns = [
    path('homepage_news/', homepage_news, name="homepage_news"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("articoli/", articoloDetailView, name="articolo_detail"),
    path("giornalisti/<int:pk>", giornalistaDetailView, name="giornalista_detail"),
    path("giornalisti/", giornalistaDetailView, name="giornalista_detail"),
    path("lista_articoli/<int:pk>", lista_articoli_giornalisti, name="lista_articoli"),
    path("lista_articoli/", lista_articoli_giornalisti, name="lista_articoli"),
    path("lista_giornalisti/", lista_giornalisti, name="lista_giornalisti"),
    path("lista_giornalisti/<int:pk>", lista_giornalisti, name="lista_giornalisti"),
    path("query_base/", query_base, name="query_base"),
    path('', index_news, name='index_news'),
    path("lista_giornalisti_api/", giornalisti_lista_api, name="list_giornalisti_api"),
    path("giornalista_api/<int:pk>", giornalista_api, name="giornalista_api"),
    
]