from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name= 'Inicio'),
    path('Proyectos/<str:proyect>', views.Proyectos,name= 'proyectos' ), 
    path('Inicio', views.inicio, name='inicio' )
]