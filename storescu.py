import sys
from pynetdicom import AE
ae = AE(ae_title=b'MY_ECHO_SCU')
ae.add_requested_context('1.2.840.10008.1.1')
addr= "127.0.0.1"
port=8999
assoc = ae.associate(addr,port)

if assoc.is_established:
    status = assoc.send_c_echo()

    if status:
        print('C-ECHO Response: 0x{0:04x}'.format(status.Status))

    assoc.release()