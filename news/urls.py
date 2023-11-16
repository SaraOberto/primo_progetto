from django.urls import path
from .views import home, articoloDetailView

app_name = 'news'

urlpatterns = [
    path('', home, name="homeview"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("lista_articoli/<int:pk>", lista_articoli_giornalisti, name="lista_articoli"),
    path("lista_articoli", lista_articoli_giornalisti, name="lista_articoli"),
    path("query", query_base, name="query"),
]