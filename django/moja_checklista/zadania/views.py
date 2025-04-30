from django.shortcuts import render, redirect, get_object_or_404
from .models import Zadanie
# Create your views here.

def lista_zadan (request):
    if request.method == 'POST':
        tresc = request.POST.get('tresc')
        if tresc:
            Zadanie.objects.create(tresc=tresc)
            
        return redirect('lista') # pozniej wraca na strone głowna
    
    
    zadania = Zadanie.objects.all()
    return render(request, 'zadania/lista.html', {'zadania': zadania})

def zmien_status(request, zadanie_id):
    zadanie = get_object_or_404(Zadanie, id=zadanie_id)
    zadanie.zrobione = not zadanie.zrobione  # zamieniamy True ↔ False
    zadanie.save()
    return redirect('lista')