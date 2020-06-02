from django import forms
from .models import *
from .logic.logic_productos import *
from usuarios.models import Paciente

class PedidoForm(forms.ModelForm):
    direccion = forms.CharField(label="Dirección", widget=forms.TextInput(
        attrs={
            "placeholder":"Introduzca su dirección"
        }
    ))
    paciente = None
    class Meta:
        model = Pedido
        fields = [
            'direccion'
        ]
    def set_paciente(self, pc:Paciente):
        self.paciente = pc

class MedicamentoPedidoForm(forms.ModelForm):
    cantidad = forms.IntegerField(label="Cantidad", widget=forms.NumberInput(
        attrs={
            'placeholder':'Introduzca la cantidad'
        }
    ))
    medicamento = forms.ModelChoiceField(label="Medicamento", queryset=get_all_products())
    pedido = forms.ModelChoiceField(label="Pedido", queryset=get_pedidos())
    class Meta:
        model = MedicamentoPedido
        fields = [
            'medicamento',
            'cantidad',
            'pedido',
        ]

class OrdenMedicaForm(forms.Form):
    numRegistro = forms.IntegerField(label='Número de Solicitud', widget=forms.NumberInput(
        attrs={
            'placeholder':'Introduzca su número de solicitud',
        }
    ))