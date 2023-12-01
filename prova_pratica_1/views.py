from django.shortcuts import render
import random

# Create your views here.
def indexP(request):
    return render(request, "indexP.html")

def somma(request):
    var1 = random.randint(1,10)
    var2 = random.randint(1,10)
    somma = var1+var2
    context = {
        'var1' : var1,
        'var2' : var2,
        'somma' : somma,
    }
    return render(request, "somma.html", context)

def media(request):
    lista = []
    i = 0
    somma = 0
    for i in range (30) :
        n=random.randint(1,10)
        lista.append(n)
        somma+=n
    media = somma/30

    context = {  
        'lista' : lista,
        'media' : media,
    }
    return render(request, "media.html", context)

def voti(request):
    
    context = {
        'dizionario' : {'studente1': 8, 'studente2': 6, 'studente3' : 7, 'studente4' : 4},
    }

    return render(request, "voti.html", context)

