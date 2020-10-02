from pydicom import dcmread
from pydicom.data import get_testdata_files
fpath = get_testdata_files("CT_small.dcm")[0]
print("Reading PyDICOM",fpath)

ds = dcmread(fpath)
print (ds)
patientNameElement = ds[0x0010,0x0010]
patientNameElement.value = "Abhijit Roy"
dateOfBirth = ds[0x0010, 0x0030]
print("------------After Changing-------------")
print(ds)
#dateOfBirth = Da("22091987")
print(dateOfBirth)

print(ds)



