from django.shortcuts import render
from django.http import HttpResponse
from .models import Articolo, Giornalista
# Create your views here.

def home(request):
    a = ""
    g = ""
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render(request, "homepage.html", context)

def articoloDetailView(request, pk):
    #articolo = Articolo.objects.get(pk=pk)
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {"articolo": articolo}
    return render(request, "articolo_detail.html", context)
    #for art in Articolo.objects.all():
        #a += (art.titolo + "<br>")
        #a.append(art.titolo)
    
    #for gio in Giornalista.objects.all():
        #g += (gio.nome + "<br>")
        #g.append(gio.nome)

    #response = "Articoli:<br>" + a + "<br>Giornalisti:<br>" + g
    #response = str(a) + "<br>" + str(g)
    #print (response)
    
    #return HttpResponse("<h1>" + response + "</h1>")
