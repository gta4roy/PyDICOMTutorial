from pydicom import dcmread
from pydicom.data import get_testdata_files
fpath = get_testdata_files("CT_small.dcm")[0]
print("Reading PyDICOM",fpath)

ds = dcmread(fpath)
print (type(ds))
#print(ds)

elem = ds[0x0008,0x0016]
print(elem)
print(elem.keyword)
private_elem = ds [0x0043,0x104E]
print(private_elem)
print(private_elem.keyword)

print("-----------------")
elem = ds[0x0008, 0x0016]
print(elem)
print(elem.value)
print(ds.SOPClassUID)
print(ds.ImageType)
print(ds[0x0008, 0x0008].VM)
print(ds.ImageType[1])


print("-----------------------")
#print(len(ds[0x0010, 0x1002]))

#for otherPatientSQElement in ds[0x0010, 0x1002]:
#    print(otherPatientSQElement)

print(ds.file_meta)
print(ds.preamble)

print("-------------------------")

print(ds.file_meta.TransferSyntaxUID)
print(ds.file_meta.TransferSyntaxUID.name)

