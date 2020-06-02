from usuarios.models import Paciente
from medicamentos.models import Medicamento
from eps.models import Cita
from eps.models import OrdenMedica
from usuarios.models import Medico
from django.core.exceptions import ObjectDoesNotExist
from habilis.views import getPutoId

def getPacientes():
    pacientes = Paciente.objects.all()
    return pacientes

def getMedicamentos():
    medicamentos = Medicamento.objects.all()
    return medicamentos

def getCitas():
    userIdMedico = getPutoId()
    try: 
        Medico.objects.get(user_id=userIdMedico)
    except ObjectDoesNotExist:
        userIdMedico = "auth0|5ea761721cc1ac0c146c32e2"
    medicoAsociaco = Medico.objects.get(user_id=userIdMedico)
    citas = Cita.objects.filter(medico = medicoAsociaco.id).order_by('-fecha')
    return citas

def getOrdenes():
    citasMedicoActual = getCitas()
    ordenes = OrdenMedica.objects.filter(cita__in = citasMedicoActual).order_by('-emision')
    return ordenes