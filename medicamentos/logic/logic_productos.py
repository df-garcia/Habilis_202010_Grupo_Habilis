from ..models import *
from django.core.exceptions import ObjectDoesNotExist

def get_pedidos():
    return Pedido.objects.all()

def get_all_products():
    productos = Medicamento.objects.all()
    return productos

def get_product(producto):
    try:
        Medicamento.objects.get(referencia=producto)
    except ObjectDoesNotExist:
        return 0
    med = Medicamento.objects.get(referencia=producto)
    return Medicamento.objects.get(referencia=producto)

def get_precio_medicamento(nombre):
    return Medicamento.objects.get(referencia=nombre).precio

# def get_pedidos(id_paciente):
#     pass