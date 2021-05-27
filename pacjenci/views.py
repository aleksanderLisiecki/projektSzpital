from django.shortcuts import render
from django.http import QueryDict
from django.db.models import Q
from django.http import HttpResponse, request
from .models import *

# request.POST = QueryDict('').copy()
# request.POST.update(request.session['search-profiles-post'])

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

def patient_info(request, patient_id):
    patient_data = Patient.objects.get(pesel=patient_id)
    patient_studies = Studies.objects.filter(patient = patient_id).order_by('-study_date')

    # for studies in patient_studies:
    #     new == Series.objects.get(study = studies.id)
    # patient_studies_filtered = []

    # rtg_on_query = request.GET.get('rtg')
    # mri_on_query = request.GET.get('mri')
    # other_on_query = request.GET.get('other_xray')
    # checkboxes = [
    #     rtg_on_query,
    #     mri_on_query,
    #     other_on_query
    # ]
    start_date_query = request.GET.get('start_date')
    end_date_query = request.GET.get('end_date')
    body_part_query = request.GET.get('body_part')
    modalities_query = request.GET.get('modality')

    if is_valid_queryparam(modalities_query):
        patient_studies = patient_studies.filter(modalities__icontains = modalities_query)

    if is_valid_queryparam(body_part_query):
        patient_studies = patient_studies.filter(body_parts__icontains = body_part_query)

    if is_valid_queryparam(start_date_query):
        patient_studies = patient_studies.filter(study_date__gte = start_date_query)

    if is_valid_queryparam(end_date_query):
        patient_studies = patient_studies.filter(study_date__lt = end_date_query)

    # modalities_query = []
    # modalities_query = request.POST.getList('modalities')
    #
    # print(modalities_query)
    # print(rtg_on_query)
    # print(mri_on_query)
    # print(other_on_query)
    # for i in checkboxes:
    #     print(i)
    #     if is_valid_queryparam(i):
    #         patient_studies_filtered += patient_studies.filter(xray_type__icontains = i)

    # print(patient_studies_filtered)
    # if patient_studies_filtered:
    #     patient_studies = patient_studies_filtered

    modalities = []
    for study in patient_studies:
        modalities.append(study.modalities)

    modalities = list(set(modalities))

    data = {
        'patient_data' : patient_data,
        'patient_studies' : patient_studies,
        'modalities': modalities
    }
    return render(request, 'patient_info.html', data)

def studies_info(request, studies_id):
    studies_data = Studies.objects.get(id=studies_id)
    studies_series = Series.objects.filter(study=studies_id)
    data = {
        'studies_data' : studies_data,
        'studies_series' : studies_series
    }
    print(studies_id)
    print(studies_series)
    return render(request, 'studies_info.html', data)

def series_info(request, series_id):
    series_data = Series.objects.get(id=series_id)
    dicom_list = DICOM.objects.filter(series=series_id)
    data = {
        'series_data' : series_data,
        'dicom_list' : dicom_list
    }
    print(dicom_list)
    return render(request, 'series_info.html', data)