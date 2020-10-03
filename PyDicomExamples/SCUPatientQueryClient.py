from pydicom.dataset import Dataset
from pynetdicom import AE, debug_logger
from pynetdicom.sop_class import GeneralRelevantPatientInformationQuery

debug_logger()

ae= AE()
ae.add_requested_context(GeneralRelevantPatientInformationQuery)

ds = Dataset()
ds.PatientName = ''
ds.PatientID ='021234567'
#ds.ContentTemplateSequence = [Dataset()]
#ds.ContentTemplateSequence[0].MappingResource = 'DCMR'
#ds.ContentTemplateSequence[0].TemplateIdentifier = '9007'

dicomAssociation = ae.associate('127.0.0.1',11113)

if dicomAssociation.is_established:
    responses = dicomAssociation.send_c_find(ds,GeneralRelevantPatientInformationQuery)
    for (status ,identifier) in responses:
        if status:
            print("C_FIND query status ")
            print(identifier)
        else:
            print('Connection timed out , was aborted or recieved invalid response ')

    dicomAssociation.release()
else:
    print("Association rejected , aborted or never connected ")

