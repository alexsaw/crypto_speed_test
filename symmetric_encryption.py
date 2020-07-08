import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

###############
# Encrypt 1000x with three different algorithms (AES, 3DES, Blowfish) and the mode, CBC (Cipher Block Chaining)
def encrypt(algo):
    # symmetric key setup and crypto library required variables
    backend = default_backend()
    iv = os.urandom(16)
    algorithm = algo['algo']
    mode_of_operation = algo['mode']
    # generate symmetric cipher (I want to make this cycle through a few encryption types and cipher modes)
    cipher = Cipher(algorithm, mode_of_operation, backend=backend)
    encryptor = cipher.encryptor() 
    plain_text = b'a secret message'
    cipher_text = encryptor.update(plain_text) + encryptor.finalize()
    
    # test decryption of the 
    # decryptor = cipher.decryptor()
    # decrypted_plain_text = decryptor.update(cipher_text) + decryptor.finalize()
    # start sending encrypted data via process_telemtry() function
    return cipher_text
###############