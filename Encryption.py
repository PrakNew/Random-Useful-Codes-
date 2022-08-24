from cryptography.fernet import Fernet

import base64, hashlib

def gen_fernet_key(passcode:bytes) -> bytes:
    assert isinstance(passcode, bytes)
    hlib = hashlib.md5()
    hlib.update(passcode)
    return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))


passcode ='any passocode'
abc=passcode.encode('utf-8')
key =gen_fernet_key(abc)
fernet = Fernet(key)
data_in = "Python"
cypher_text = fernet.encrypt(data_in.encode('utf-8'))
decr_data = fernet.decrypt(cypher_text).decode('utf-8')
