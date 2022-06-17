import os
from cryptography.fernet import Fernet

# encryt key
KEY_FILE = os.path.join(os.path.dirname(__file__),'..', 'config', '.ENCRYPT_KEY')
ENCRYPT_KEY = os.getenv('ENCRYPT_KEY')
if ENCRYPT_KEY is None:
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE) as f:
            ENCRYPT_KEY = f.read()
    else:
        ENCRYPT_KEY = Fernet.generate_key().decode()
        with open(KEY_FILE, 'w') as f:
            f.write(ENCRYPT_KEY) 
ENCRYPT_KEY = ENCRYPT_KEY.encode()