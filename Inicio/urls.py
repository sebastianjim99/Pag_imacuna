from xml.dom.minidom import Document
from django.urls import path
from . import views
from django.conf import settings 
from django.contrib.staticfiles.urls import static 


urlpatterns = [

    path('', views.inicio, name= 'Inicio'),
    path('Lineas_investigacion', views.lineas_inves, name= 'Lineas_investigacion'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)