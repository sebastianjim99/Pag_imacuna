from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse ('Hello world')

def Proyectos(request, proyect):
    items = {
        'Proyecto1': 'Nombre 1',
        'Proyecto2': 'Nombre 1',
        'Proyecto3': 'Nombre 1',
        'Proyecto4': 'Nombre 1',
    }
    description = items[proyect]
    return HttpResponse (f"<h2> {proyect} </h2>" + description)