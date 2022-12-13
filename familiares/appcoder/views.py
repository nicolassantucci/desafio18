from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse

def familiares(request):
    familiar =Familiar(nombre="nicolas",edad=30,fecha="1992-06-06")
    familiar.save()
    cadena_texto="familiar guardado:"+str(familiar) 
    return HttpResponse(cadena_texto)
