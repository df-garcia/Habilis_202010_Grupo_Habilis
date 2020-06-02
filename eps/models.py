from django.db import models

# Clase EPS
class Eps(models.Model):
    #Atributos
    nombre = models.CharField( max_length=40 , default='Sin nombre', null=True, blank=True)

    #Métodos
    def __str__(self):
        return '{}'.format(self.nombre)

# Clase Cita
class Cita(models.Model):
    #Atributos
    tipo = models.CharField( max_length=40 , default='Sin nombre', null=True, blank=True)
    fecha = models.DateTimeField(null=True, blank=True)

    #Relaciones
    medico = models.ForeignKey('usuarios.Medico', on_delete=models.CASCADE , null = True, blank=True, default=None)
    paciente = models.ForeignKey('usuarios.Paciente', on_delete=models.CASCADE , null = False, blank=True, default=None)
    
    #Métodos
    def __str__(self):
        return '{}'.format(self.tipo + "("+self.fecha.__str__()+")")

# Clase OrdenMedica
class OrdenMedica(models.Model):
    #Atributos
    numRegistro = models.BigIntegerField(null=True, blank=True)
    emision = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    caducidad = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    #Relaciones
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE , null = True, blank=True, default=None)
    medicamentos = models.ManyToManyField('medicamentos.Medicamento', blank=True)
    
    #Métodos
    def __str__(self):
        return '{}'.format(self.numRegistro.__str__() + "("+self.emision.__str__() + "-" + self.caducidad.__str__()+")")