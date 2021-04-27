from django.contrib import admin
from .models import Patient, Studies, Series, DICOM

# Register your models here.

admin.site.register(Patient)
admin.site.register(Studies)
admin.site.register(Series)
admin.site.register(DICOM)
