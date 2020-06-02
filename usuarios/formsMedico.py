from django import forms
from .logic.logicMedico import *
from .models import *
from eps.models import OrdenMedica
from django.http import HttpRequest
from habilis.views import getPutoId
from .logic.logicMedico import *
from django.core.exceptions import ObjectDoesNotExist
import datetime


class FormularioOrdenMedica(forms.ModelForm):


    userIdMedico = getPutoId()
    try: 
        Medico.objects.get(user_id=userIdMedico)
    except ObjectDoesNotExist:
        userIdMedico = "auth0|5ea761721cc1ac0c146c32e2"   
    medicoAsociaco = Medico.objects.get(user_id=userIdMedico)
    

    nombreMedico = forms.CharField(label="Nombre Médico", initial=medicoAsociaco.nombre, disabled = True)
    especialidad = forms.CharField(label="Especialidad", initial=medicoAsociaco.especialidad, disabled = True)
    edad = forms.CharField(label="Edad", initial=medicoAsociaco.edad, disabled = True)
    registroMedico = forms.CharField(label="Número de registro médico", initial=medicoAsociaco.regMedico, disabled = True)
    numRegistro = forms.IntegerField(label="Número de registro de orden")
    emision = forms.DateField(label="Fecha de emision")
    caducidad = forms.DateField(label="Fecha de caducidad")
    cita = forms.ModelChoiceField(label="Cita", queryset=getCitas())
    medicamentos = forms.ModelMultipleChoiceField(label="Medicamento", queryset=getMedicamentos())

    class Meta:
        model = OrdenMedica
        fields = [
            'numRegistro',
            'emision',
            'caducidad',
            'cita',
            'medicamentos'
        ]
