from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    return render(request, 'main.html')

def patient_list(request):
    patients = Patient.objects.all()
    data = {
        'patients' : patients
    }
    return render(request, 'patient_list.html', data)

def patient_info(request, id):
    patient_data = Patient.objects.get(pesel=id)
    patient_studies = Studies.objects.filter(patient = id)
    data = {
        'patient_data' : patient_data,
        'patient_studies' : patient_studies
    }
    return render(request, 'patient_info.html', data)

def studies_info(request, id):
    studies_data = Studies.objects.get(pk=id)
    studies_series = Series.objects.filter(pk = id)
    data = {
        'studies_data' : studies_data,
        'studies_series' : studies_series
    }
    return render(request, 'studies_info.html', data)

def series_info(request, id):
    series_data = Series.objects.get(pk=id)
    dicom_list = DICOM.objects.filter(pk = id)
    data = {
        'series_data' : series_data,
        'dicom_list' : dicom_list
    }
    return render(request, 'series_info.html', data)