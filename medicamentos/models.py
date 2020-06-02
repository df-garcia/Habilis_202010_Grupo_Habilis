from django.db import models

# Create your models here.

class Pedido(models.Model):
    #Atributos
    fecha = models.DateField(auto_now_add=True, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    precioTotal = models.FloatField(null=True, blank=True)
    #Relaciones
    paciente = models.ForeignKey('usuarios.Paciente', on_delete=models.CASCADE, null=True, blank=True)
    #Funciones
    def __str__(self):
        return '%s' % (self.direccion)

class Medicamento(models.Model):
    #Atributos
    referencia = models.CharField(max_length=120, null=True, blank=True)
    descripcion = models.CharField(max_length=200,null=True, blank=True)
    indicaciones = models.CharField(max_length=250,null=True, blank=True)
    precio = models.FloatField()
    
    #Métodos
    def __str__(self):
        return '{}'.format(self.referencia)

class MedicamentoPedido(models.Model):
    #Atributos
    cantidad= models.SmallIntegerField(null=True, blank=True)
    #Relaciones
    medicamento = models.OneToOneField(Medicamento, on_delete = models.CASCADE, primary_key = True, null=False, blank=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE , null = False , default=None, blank=True)
    #Métodos
    def __str__(self):
        return '%s Cantidad: %s' % (self.medicamento.__str__(), self.cantidad)

    def precio_total(self):
        return self.cantidad*self.medicamento.precio