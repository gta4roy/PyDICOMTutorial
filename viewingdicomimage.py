from pydicom import dcmread
from pydicom.data import get_testdata_files
import dicom 
import pylab 
fpath = get_testdata_files("CT_small.dcm")[0]
print("Reading PyDICOM",fpath)
ds = dcmread(fpath)
pylab.imshow(ds.pixel_array, cmap=pylab.cm.bone)
pylab.show()
print (ds)



