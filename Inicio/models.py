from distutils.command.upload import upload
from turtle import update
from django.db import models

# Create your models here.


# Modelo de lineas de investigacion 
class Lineas_investigacion(models.Model):
    id = models.AutoField(primary_key= True)
    imagen = models.ImageField(upload_to='iconos/', verbose_name="imagen", null= True, blank=True)
    descripccion = models.TextField(max_length=250 , verbose_name="Descripción", null=True)

    def __str__(self):
        fila =  str(self.id) + " - " +  str(self.imagen) +  " - " + "Descripción: " + self.descripccion
        return fila


    def delete(self, using= None, keep_parents = False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

    
