from django.shortcuts import render,redirect
from django.db.models import Q # new
#From Logic
# Create your views here.
from django.views import View
from django.views.generic import ListView
from .logic import *
from eps.models import OrdenMedica
from medicamentos.forms import *

class PedidoCreateView(View):
    template_name = 'pedidos/create.html'
    def get(self, request, *args, **kwargs):
        form = PedidoForm()
        context = {'form':form}
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            form = PedidoForm()
        context = {"form":form}
        return render(request, self.template_name, context)

class CreateMedicamentoProductoView(View):
    template_name = 'productos/slectProducto.html'
    def get(self, request, *args, **kwargs):
        form = MedicamentoPedidoForm()
        context = {'form':form}
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        form = MedicamentoPedidoForm(request.POST)
        if form.is_valid():
            form.save()
            form = MedicamentoPedidoForm()
        context = {"form":form}
        return render(request, self.template_name, context)

class ValidarOrdenMedicaView(View):
    template_name = 'orden_medica/validar_orden.html'
    def get(self, request, *args, **kwargs):
        form = OrdenMedicaForm()
        context = {
            'form':form
        }
        return render(request, self.template_name, context)

class VerOrdenMedicaView(View):
    template_name = 'orden_medica/orden_encontrada.html'
    def get(self, request):
        numReg = int(request.GET['q'])
        try:
            orden = OrdenMedica.objects.get(numRegistro=numReg)
        except:
            orden = None
        medicamentos = None
        if orden != None:
            medicamentos = orden.medicamentos.all()
        context = {
            'orden':orden,
            'meds':medicamentos,
        }
        return render(request, self.template_name, context)

class ConsultarPedidosView(View):
    template_name = 'orden_medica/consultar.html'
    """
    def get(self, request, **kwargs):
        pedidos = get_pedidos(kwargs['id'])
        context = {
            'pedidos':pedidos
        }
        return render(request, self.template_name, context)
    """
    def get(self, request):
        return render(request, self.template_name, {})