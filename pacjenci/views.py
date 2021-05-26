from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from .models import *

def is_valid_queryparam(param):
    return param != '' and param is not None

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
    patient_studies = Studies.objects.filter(patient = id).order_by('-study_date')
    
    patient_studies_filtered = []

    rtg_on_query = request.GET.get('rtg')
    mri_on_query = request.GET.get('mri')
    other_on_query = request.GET.get('other_xray')
    checkboxes = [
        rtg_on_query,
        mri_on_query,
        other_on_query
    ]
    start_date_query = request.GET.get('start_date')
    end_date_query = request.GET.get('end_date')
    body_part_query = request.GET.get('body_part')

    if is_valid_queryparam(body_part_query):
        patient_studies = patient_studies.filter(body_parts__icontains = body_part_query)

    if is_valid_queryparam(start_date_query):
        patient_studies = patient_studies.filter(study_date__gte = start_date_query)

    if is_valid_queryparam(end_date_query):
        patient_studies = patient_studies.filter(study_date__lt = end_date_query)
    # print(checkboxes)
    # print(rtg_on_query)
    # print(mri_on_query)
    # print(other_on_query)
    for i in checkboxes:
        print(i)
        if is_valid_queryparam(i):
            patient_studies_filtered += patient_studies.filter(xray_type__icontains = i)

    # print(patient_studies_filtered)
    if patient_studies_filtered:
        patient_studies = patient_studies_filtered
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