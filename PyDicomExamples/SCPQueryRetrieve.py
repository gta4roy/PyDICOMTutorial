import os 
from pydicom import dcmread
from pynetdicom import AE,evt 
from pynetdicom.sop_class import PatientRootQueryRetrieveInformationModelFind

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

    if 'QueryRetrieveLevel' not in queryDataSet:
        yield 0xC000, None 
        return 
        
    responseSopObjects= []
    for sopObjects in sopInstances:
        if queryDataSet.QueryRetrieveLevel == 'PATIENT' and sopObjects.PatientID == queryDataSet.PatientID:
            responseSopObjects.append(sopObjects)
            print("Success Query")

    yield(0xFF00,responseSopObjects[0])

handlers = [(evt.EVT_C_FIND,handle_find)]

#setup configurations
ae= AE()
ae.add_supported_context(PatientRootQueryRetrieveInformationModelFind)
print("Query Retieve  Server started....")
ae.start_server(('127.0.0.1',11114),evt_handlers=handlers)