from django.shortcuts import render
from .models import Zadanie
# Create your views here.

def lista_zadan (request):
    zadania = Zadanie.objects.all()
    return render(request, 'zadania/lista.html', {'zadania': zadania})
