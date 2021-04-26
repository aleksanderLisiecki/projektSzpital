from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    dicom_location = models.TextField(blank=True)
    dicom_file = models.FileField(blank=True, default=None, null=True)

    def __str__(self):
        return self.name + ' '