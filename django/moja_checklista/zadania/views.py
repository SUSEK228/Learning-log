from django.shortcuts import render, redirect
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
