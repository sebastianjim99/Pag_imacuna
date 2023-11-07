from django.shortcuts import render
from django.http import HttpResponse
from .models import Lineas_investigacion

# Create your views here.

def inicio(request):
    investigacion= Lineas_investigacion.objects.all()
    return render(request, 'inicio.html', {'investigacion': investigacion})

def lineas_inves(request):
    return render(request, 'Admin/Lineas_inves.html')