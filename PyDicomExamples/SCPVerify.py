#handling the C ECHO request 
#Verification SOP 

from pynetdicom import AE ,evt ,VerificationPresentationContexts
from pynetdicom.sop_class import VerificationSOPClass

#create a Hanlder 
def handle_echo(event):
    print("C-ECHO Request Recieved ")
    return 0x0000

#initialise application AE 
ae = AE()
#Add supported Presentation context 
ae.supported_contexts= VerificationPresentationContexts
ae.add_requested_context(VerificationSOPClass)

handlers = [(evt.EVT_C_ECHO,handle_echo)]
print("Verification SCP service listening at 11112...")
ae.start_server(('',11112),evt_handlers=handlers)


