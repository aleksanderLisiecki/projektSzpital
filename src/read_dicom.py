import pydicom

# more info on Value Representations (VR) on: http://dicom.nema.org/dicom/2013/output/chtml/part05/sect_6.2.html

STUDY_DATE = 0x00080020  # DA
PATIENT_AGE = 0x00101010  # AS
MODALITY = 0x00080060  # CS
BODY_PART = 0x00180015  # CS
SERIES_NUM = 0x00200011  # IS
SERIES_DATE = 0x00080021  # DA
SERIES_DESCRIPTION = 0x0008103e  # LO
INSTANCE_NUMBER = 0x00200013  # IS

class DicomReader:
    study_date = ''
    patient_age = ''
    modality = ''
    body_part = ''
    series_num = ''
    series_date = ''
    series_description = ''
    instance_number = ''

    def __init__(self, dicom_file):
        self.study_date = self._getValue(dicom_file, STUDY_DATE)
        self.patient_age = self._getValue(dicom_file, PATIENT_AGE)
        self.modality = self._getValue(dicom_file, MODALITY)
        self.body_part = self._getValue(dicom_file, BODY_PART)
        self.series_num = self._getValue(dicom_file, SERIES_NUM)
        self.series_date = self._getValue(dicom_file, SERIES_DATE)
        self.series_description = self._getValue(dicom_file, SERIES_DESCRIPTION)
        self.instance_number = self._getValue(dicom_file, INSTANCE_NUMBER)

    def _getValue(self, dicom_file, attribute_val):
        return dicom_file[attribute_val].value



# patient_age = int(dickom.patient_age[:3])

# print(date)
# print(age)
# print(dickom.modality)
# print(dickom.body_part)
# print(dickom.series_num)
# print(series_date)
# print(series_description)
# print(dickom.instance_number)

# st = Studies(name=dickom.series_description, study_date=study_date, age=patient_age, modalities=dickom.modality)
# st.save()
# se = Series(series_num=dickom.series_num, date=series_date, body_part=dickom.body_part,
#             description=dickom.series_description, study=st.id).save()
# se.save()
# DICOM(instance=dickom.instance_number, location=file_path, series=se.id).save()
