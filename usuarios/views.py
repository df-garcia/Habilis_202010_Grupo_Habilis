from django.shortcuts import render,redirect
from django.views import View
from usuarios.formsMedico import FormularioOrdenMedica
from habilis.auth0backend import getRole, getUserId
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from usuarios.logic.logicMedico import getCitas
from usuarios.logic.logicMedico import getOrdenes

class FormularioOrdenView(View):
    template_name = 'medico2.html'
    def get(self, request, *args, **kwargs):
        form = FormularioOrdenMedica()
        context = {'form':form}
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        form = FormularioOrdenMedica(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Orden creada con éxito!')  
            form = FormularioOrdenMedica()
        context = {"form":form}
        return render(request, self.template_name, context)

class VisualizacionCitas(View):
    template_name = 'medicoCitas.html'
    def get(self, request):
        citas = getCitas()
        data = citas.values('id', 'tipo', 'fecha', 'medico', 'medico__nombre', 'paciente', 'paciente__nombre')
        context = {
            'tags': [
                {'citas': data}
            ]
        }
        return render(request, self.template_name, context)

class VisualizacionOrdenes(View):
    template_name = 'medicoOrdenes.html'
    def get(self, request):
        data = getOrdenes()
        #data = ordenes.values('id', 'numRegistro', 'emision', 'caducidad', 'cita', 'cita__id', 'cita__paciente__nombre','medicamentos')
        #data = ordenes.values()
        context = {
            'tags': [
                {'ordenes': data}
            ]
        }
        return render(request, self.template_name, context)

class UIPaciente(View):
    template_name = 'ui_paciente.html'
    def get(self, request):
        return render(request, self.template_name, {})