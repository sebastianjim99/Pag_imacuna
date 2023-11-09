from dataclasses import field
from socket import fromshare
from django import forms
from .models import Lineas_investigacion


class Linea_Form (forms.ModelForm):
    class Meta:
        model = Lineas_investigacion
        fields = '__all__'