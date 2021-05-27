from django.db import models


class Patient(models.Model):
    class Meta:
        verbose_name_plural = "Patients"

    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    pesel = models.CharField(max_length=11, primary_key=True)
    first_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    birthdate = models.DateField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    phone_no = models.CharField(max_length=15, blank=True)

    # address
    street_name = models.CharField(max_length=20, blank=True)
    house_no = models.IntegerField(blank=True)
    flat_no = models.IntegerField(blank=True)
    postal_code = models.CharField(max_length=6, blank=True)
    city = models.CharField(max_length=20, blank=True)

    description = models.TextField(blank=True)
    dicom_location = models.TextField(blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.surname


class Studies(models.Model):
    class Meta:
        verbose_name_plural = "Studies"

    name = models.CharField(max_length=50)
    study_date = models.DateField()
    age = models.IntegerField(blank=True)
    modalities = models.CharField(max_length=30, blank=True)
    body_parts = models.CharField(max_length=50, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient.__str__() + '/' + self.name


class Series(models.Model):
    class Meta:
        verbose_name_plural = "Series"
    series_num = models.IntegerField()
    date = models.DateField()
    body_part = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)
    comment = models.TextField(blank=True)
    study = models.ForeignKey(Studies, on_delete=models.CASCADE)

    def __str__(self):
        return self.study.__str__() + '/' + str(self.series_num)


class DICOM(models.Model):
    class Meta:
        verbose_name_plural = "DICOM"
    instance = models.IntegerField(blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    dicom_file = models.FileField(blank=True, default=None, null=True)

    def __str__(self):
        return self.series.__str__() + '/' + str(self.instance)

    def save(self, *args, **kwargs):

        description = ''
        description += 'Location: ' + str(self.dicom_file.path) + ','

        self.description = description
        super(DICOM, self).save(*args, **kwargs)
