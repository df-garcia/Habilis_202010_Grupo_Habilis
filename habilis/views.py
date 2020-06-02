from django.http import HttpResponse
from django.shortcuts import render
from habilis.auth0backend import getRole, getUserId
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'base.html')

userId = ""

@login_required
def measurement_list(request):
    role = getRole(request)
    global userId
    userId = getUserId(request)

    if role == "Médico":
        return render(request,'medico.html')

    elif role == "Paciente":
        return render(request,'paciente.html')
    else:
        return HttpResponse("Unauthorized User")

def getPutoId():
    measurement_list
    return str(userId)

