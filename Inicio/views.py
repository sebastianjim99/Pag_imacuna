from multiprocessing import context
from unicodedata import digit
from django.shortcuts import render
from django.http import HttpResponse
from .models import Lineas_investigacion
from .forms import Linea_Form

# Create your views here.

def inicio(request):
    investigacion= Lineas_investigacion.objects.all()
    return render(request, 'inicio.html', {'investigacion': investigacion})

def admin(request):
    investigacion= Lineas_investigacion.objects.all()
    return render(request, 'Admin.html', {'investigacion': investigacion})

def editar(request):
    return render(request, 'Admin/editar.html') 


def Crear(request):
    formulario = Linea_Form(request.POST or None)
    return render(request, 'Admin/Crear.html', {'formulario': formulario})


