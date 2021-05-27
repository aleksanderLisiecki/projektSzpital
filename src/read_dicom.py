import pydicom

# more info on Value Representations (VR) on: http://dicom.nema.org/dicom/2013/output/chtml/part05/sect_6.2.html

PATIENTS_NAME = 0x00100010 # VR: PN - 64 chars maximum per component group
PATIENT_ID = 0x00100020 # VR: LO - 64 chars maximum
PATIENTS_BIRTH_DATE = 0x00100030 # VR: DA - 8 bytes fixed
PATIENTS_SEX = 0x00100040 # VR: CS - 16 bytes maximum

file_path = 'C:/Users/alili/Desktop/medical-images-examples/Projekt/Rezonans Magnetyczny/Monkiewicz_Michal/Mr_Mozgu_I_Pnia_Mozgu_Bez - 429748/Apparent_Diffusion_Coefficient_(mm2s)_900/IM-0015-0001.dcm'

dicom_file = pydicom.filereader.dcmread(file_path)

class DicomReader:
    patients_name = ''
    patient_id = ''
    patients_birth_date = ''
    patients_sex = ''

    def __init__(self, dicom_file):
        self.patients_name = self._getValue(dicom_file, PATIENTS_NAME)
        self.patient_id = self._getValue(dicom_file, PATIENT_ID)
        self.patients_birth_date = self._getValue(dicom_file, PATIENTS_BIRTH_DATE)
        self.patients_sex = self._getValue(dicom_file, PATIENTS_SEX)


    def _getValue(self, dicom_file, attribute_val):
        return dicom_file[attribute_val].value


dickom = DicomReader(dicom_file)

print(dickom.patients_name)
print(dickom.patient_id)
print(dickom.patients_birth_date)
print(dickom.patients_sex)