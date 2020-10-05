from pydicom.dataset import Dataset
from pynetdicom import AE, debug_logger
from pynetdicom.sop_class import PatientRootQueryRetrieveInformationModelFind

debug_logger()

ae= AE()
ae.add_requested_context(PatientRootQueryRetrieveInformationModelFind)

ds = Dataset()
ds.PatientName = ''
ds.PatientID ='021234567'

dicomAssociation = ae.associate('127.0.0.1',11114)

if dicomAssociation.is_established:
    responses = dicomAssociation.send_c_find(ds,PatientRootQueryRetrieveInformationModelFind)
    for (status ,identifier) in responses:
        if status:
            print("C_FIND query status ")
            print(identifier)
        else:
            print('Connection timed out , was aborted or recieved invalid response ')

    dicomAssociation.release()
else:
    print("Association rejected , aborted or never connected ")

