from django.db import models

# Create your models here.

class Usuario(models.Model):
    #Atributos
    cedula = models.BigIntegerField(null=True, blank=True)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    celular = models.CharField(max_length=50, null=True, blank=True)
    correo = models.CharField(max_length=50, null=True, blank=True)

class Paciente(Usuario):
    #Atributos
    edad = models.IntegerField(null=True, blank=True)
    #Relaciones
    eps = models.ForeignKey('eps.Eps', on_delete=models.CASCADE, null=True, blank=True)
    #Funciones
    def __str__(self):
        return '{}'.format(self.nombre + "("+self.cedula.__str__()+")")

class Medico(Usuario):
    #Atributos 
    user_id = models.CharField(max_length=150, null=True, blank=True)
    regMedico= models.CharField(max_length=100, null=True, blank=True)
    edad= models.SmallIntegerField(null=True, blank=True)
    especialidad= models.CharField(max_length=120, null=True, blank=True)
    #Relaciones:
    eps = models.ManyToManyField('eps.Eps', blank=True)
    #Métodos
    def __str__(self):
        return '{}'.format(self.regMedico + "("+self.especialidad+")")
