import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from pathlib import Path


def generate():
    # reading card file
    temp = Path('temp')
    if temp.is_file():
        with open('temp', 'r') as f:
            lines = f.readlines()
            card_number = lines[0]
            pin = lines[1]
    else:
        print('ERROR: temp file not found')
    # generating the keys
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    print('Private Key generated')
    public_key = private_key.public_key()
    print('Public Key generated')

    # Storing private_key
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    with open('private-keys/' + f'{card_number}.pvk', 'wb') as f:
        f.write(pem)
        print('Private Key Stored')

    # Storing public_key
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open('public-keys/' + f'{card_number}.pbk', 'wb') as f:
        f.write(pem)
        print('Public Key stored')
    os.remove('temp')
