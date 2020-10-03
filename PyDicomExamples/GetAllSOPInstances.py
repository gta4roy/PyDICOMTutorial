import os 
from pydicom import dcmread
from pydicom.dataset import Dataset

def getAllSopInstances():
    SOPInstances = []
    fdir = './SOPDIR/'

    for fpath in os.listdir(fdir):
        try:
            SOPInstances.append(dcmread(os.path.join(fdir,fpath))) 
        except:
            pass
    return SOPInstances

#for dicomInstance in getAllSopInstances():
#    print(dicomInstance.PatientID,dicomInstance.PatientName)




