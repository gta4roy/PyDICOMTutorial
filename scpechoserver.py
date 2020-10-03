from pynetdicom import AE , VerificationPresentationContexts
ae = AE(ae_title=b'MY_ECHO_SCP')
ae.supported_contexts= VerificationPresentationContexts
ae.start_server(('127.0.0.1',8999),block=True)