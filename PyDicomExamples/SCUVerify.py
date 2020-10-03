from pynetdicom import AE ,evt ,VerificationPresentationContexts
from pynetdicom.sop_class import VerificationSOPClass


#initialise application AE 
ae = AE()
#Add supported Presentation context 
ae.supported_contexts= VerificationPresentationContexts
ae.add_requested_context(VerificationSOPClass)

#Create a association with SCP 
dicomAssociation = ae.associate('127.0.0.1',11112)

if dicomAssociation.is_established:
    status = dicomAssociation.send_c_echo()

    if status:
        print('C Echo request status : 0x{0:04x}',format(status.Status))

    else:
        print('Connection timed out, was abborted or recieved invalid response ')

    dicomAssociation.release()
else:
    print('Association Rejected , aborted or never connected ')