from django.urls import path
from . import views


urlpatterns = [
    path('Proyectos/<str:proyect>', views.Proyectos),
]