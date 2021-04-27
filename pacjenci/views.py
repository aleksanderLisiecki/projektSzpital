from django.shortcuts import render
from django.http import HttpResponse
from .models import Patient


def index(request):
    return render(request, 'main.html')

def patient_list(request):
    patients = Patient.objects.all()
    data = {
        'patients' : patients
    }
    return render(request, 'patient_list.html', data)

def patient_info(request, id):
    patient_data = Patient.objects.get(pk=id)
    data = {
        'patient_data' : patient_data
    }
    return render(request, 'patient_info.html', data)