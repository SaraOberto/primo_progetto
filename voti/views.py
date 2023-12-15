from django.shortcuts import render

# Create your views here.

diz_studenti = {
           'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]
        } 

def indexV(request):
    return render(request, "indexV.html")

def view_a(request):
    context = {
       'materie': ["Matematica","Italiano","Inglese","Storia","Geografia"] 
    }
    return render(request, "view_a.html", context)

def view_b(request):
    context = {
        'diz_studenti' : diz_studenti,
    }
    return render(request, "view_b.html", context)

def view_c(request):
    i = 0
    j = 0
    somma = 0
    lista = []
    for studenti,materie in diz_studenti:
        somma=0
        for materia,voto in materie:
            somma += voto
        media = somma/materia
        lista.append(media)
    context = {  
    'lista' : lista,
    }
    return render(request, "view_c.html", context)
    
def view_d(request):

    return render(request, "view_d.html", context)


