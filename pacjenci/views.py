from django.shortcuts import render
from django.http import HttpResponse
from .models import Patient


def index(request):
    return HttpResponse(Patient.objects.all())

