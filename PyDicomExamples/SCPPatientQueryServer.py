import os 
from pydicom import dcmread 
from pydicom.dataset import Dataset

from pynetdicom import AE, evt 
from pynetdicom.sop_class import GeneralRelevantPatientInformationQuery

def getAllSopInstances():
    SOPInstances = []
    fdir = './SOPDIR/'

    for fpath in os.listdir(fdir):
        try:
            SOPInstances.append(dcmread(os.path.join(fdir,fpath))) 
        except:
            pass
    return SOPInstances

def handle_find(event):
    print("C_FIND request Received ")
    sopInstances = getAllSopInstances()
    queryDataSet = event.identifier 

    responseSopObjects= []
    for sopObjects in sopInstances:
        if sopObjects.PatientID == queryDataSet.PatientID:
            responseSopObjects.append(sopObjects)
            print("Success Query")

    yield(0xFF00,responseSopObjects[0])
        
handlers = [(evt.EVT_C_FIND,handle_find)]

ae= AE()
ae.add_supported_context(GeneralRelevantPatientInformationQuery)
print("C_FIND Server started....")
ae.start_server(('127.0.0.1',11113),evt_handlers=handlers)


