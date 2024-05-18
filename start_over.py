import os

try:
    # delete everything in gen_certs folder
    for cert in os.listdir('gen_certs'):
        cert_path = os.path.join('gen_certs', cert)
        os.remove(cert_path)

    # delete everything in gen_certs_with_qr folder
    for cert in os.listdir('gen_certs_with_qr'):
        cert_path = os.path.join('gen_certs_with_qr', cert)
        os.remove(cert_path)

    # delete everything in uploads folder
    for cert in os.listdir('uploads'):
        cert_path = os.path.join('uploads', cert)
        os.remove(cert_path)

    # delete certificates.csv
    os.remove('certificates.csv')

    # delete compiled_code.json
    os.remove('compiled_code.json')
except:
    pass
