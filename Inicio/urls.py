from xml.dom.minidom import Document
from django.urls import path
from . import views
from django.conf import settings 
from django.contrib.staticfiles.urls import static 


urlpatterns = [
    path('', views.inicio, name= 'Inicio'),
    path('Admin', views.admin, name= 'Admin'),
    path('Admin/crear', views.Crear, name= 'Crear' ),
    path('editar', views.editar, name= 'Editar'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)