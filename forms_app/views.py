from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormContatto
from .models import Contatto
from django.shortcuts import get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required



def contatti(request):
    if request.method == "POST":
        form = FormContatto(request.POST)
        if form.is_valid():
            print("Il Form è Valido!")
            print("NOME: ", form.cleaned_data["nome"])
            print("COGNOME: ", form.cleaned_data["cognome"])
            print("EMAIL: ", form.cleaned_data["email"])
            print("CONTENUTO: ", form.cleaned_data["contenuto"])
            print("salvo il contatto nel database")
            nuovo_contatto = form.save()
            print("new_post: ", nuovo_contatto)
            print(nuovo_contatto.nome)
            print(nuovo_contatto.cognome)
            print(nuovo_contatto.email)
            print(nuovo_contatto.contenuto)
            return HttpResponse("<h1>Grazie per averci contattato!</h1>")
    else:
        form = FormContatto()

    context = {"form":form}
    return render(request, "contatto.html", context)

def lista_contatti(request, pk=None):
    if(pk==None):
        contatti=Contatto.objects.all()
    else:
        contatti=Contatto.objects.filter(contatto_id=pk)
    context = {
        'contatti': contatti,
        'pk':pk,
    }
    return render(request, 'lista_contatti.html', context)


@login_required(login_url = "/accounts/login")
def modifica_contatto(request, pk):
    contatto = get_object_or_404(Contatto, id=pk)
    if request.method == "GET":
        form = FormContatto(instance=contatto)
    if request.method =="POST":
        form = FormContatto(request.POST, instance=contatto)
        if form.is_valid():
            form.save()
            return redirect('forms_app:lista_contatti')
    context={'form':form, 'contatto':contatto}
    return render(request, 'modifica_contatto.html', context)
    
@staff_member_required(login_url = "/accounts/login")
def elimina_contatto(request, pk):
    contatto= get_object_or_404(Contatto, id=pk)
    if request.method =="POST":
        contatto.delete()
        return redirect('forms_app:lista_contatti')
    context = {'contatto':contatto}
    return render(request, 'elimina_contatto.html', context)

   
   