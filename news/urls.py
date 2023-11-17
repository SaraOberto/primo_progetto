from django.urls import path
from .views import *

app_name = 'news'

urlpatterns = [
    path('homepage_news/', homepage_news, name="homepage_news"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("articoli/", articoloDetailView, name="articolo_detail"),
    path("lista_articoli/<int:pk>", lista_articoli_giornalisti, name="lista_articoli"),
    path("lista_articoli/", lista_articoli_giornalisti, name="lista_articoli"),
    path("query_base/", query_base, name="query_base"),
]