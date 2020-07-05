################################
# This program simulates an IOT that collects data from a connected sensor and sends the data in an encrypted format to another device. it usees the cryptogrpahy library heavily: https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/#
################################

# dependencies
import os
import platform
from uuid import getnode as get_mac
import json
import time
import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# /dependencies

###############
# identify the device this is running on
def device_profile():
    # create devide profile object
    device_data = {
        # operating system 
        "os": {
            # identify device os
            "name": platform.system(),
            # identify device os release
            "release": platform.release(),
            # identify device os release version
            "release_version": platform.version()
        },
        # identify device processor
        "processor": platform.processor(),
        # identify device mac address
        "mac_address": get_mac()
    }
    # convert the dictionary into a proper JSON object
    # device_json = json.dumps(device_data, indent=4, sort_keys=False)
    
    # function returns a JSON object or dict (if json.dumps() is commented) that describes the device this script is being run on
    return device_data
###############
#print(device_profile())


###############
# Deliver sensor events as quickly as you want to simulate a sensor event
def sensor_simulator(event_frequency):
    events = 1000
    while events >= 0:
        
        events -= 1
###############
#sensor_simulator(x)


###############
# generate a private key
def gen_rsa_key():
    # crypto library required variables
    backend = default_backend()
    # generate a private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
        backend=backend
    )
    # generate a public key
    public_key = private_key.public_key()
    # send over public key, message, and signed message
    message = b"asdadw"
    signed_message = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
            hashes.SHA256()
        )
    # verify signature
    verification_result = public_key.verify(
        signed_message,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print(verification_result)
###############
gen_rsa_key()




###############
# Encrypt 1000x with three different algorithms (AES, 3DES, Blowfish) and the mode, CBC (Cipher Block Chaining)
def symmetric_encryption(algo):
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
# process sensor telemetry (encrypt and send to database)
def process_telemetry(device_details):
    # initialize row for database entry
    new_row = {
        "device": device_details,
        "algo": None,
        "start_time": None,
        "end_time": None,
        "total_time": None,
        "sensor_data": "b'a secret message'",
        "cypher_text": None,
        "test_number": None
    }
    # convert the dictionary into a proper JSON object
    # json_row = json.dumps(new_row, indent=4, sort_keys=False)
    # generate keys
    backend = default_backend()   
    salt = os.urandom(16)
    # AES key derivation fucntion and key
    aes_kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=backend
    )
    aes_key = aes_kdf.derive(b"password")
    # 3DES key derivation fucntion and key
    des3_kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=24,
        salt=salt,
        iterations=100000,
        backend=backend
    )
    des3_key = des3_kdf.derive(b"password")
    # SEED key derivation fucntion and key
    seed_kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=16,
        salt=salt,
        iterations=100000,
        backend=backend
    )
    seed_key = seed_kdf.derive(b"password")

    # cycle through three encryption algorithms (AES, 3DES, and SEED)
    algos = {
        "AES": {
            'algo': algorithms.AES(aes_key),
            'mode': modes.CBC(os.urandom(16)) 
        },
        "3DES": {
            'algo': algorithms.TripleDES(des3_key),
            'mode': modes.CBC(os.urandom(8))
        },
        "SEED": {
            'algo': algorithms.SEED(seed_key),
            'mode': modes.CBC(os.urandom(16))
        }
    }
    for selected_algo in algos:
        # go through each algorithm and run the test for each one 10x
        times_to_repeat = 10
        i = 0
        new_row['algo'] = selected_algo
        while times_to_repeat >= i:
            # choose an algorithm for the test
            algorithm_with_key = algos[selected_algo]
            # record start time
            new_row['start_time'] = int(round(time.time() * 100000))
            # encrypt the data
            new_row['cypher_text'] = symmetric_encryption(algorithm_with_key)[0]
            # connect to database
            # record end time
            new_row['end_time'] = int(round(time.time() * 100000))
            # subtract end from start time
            new_row['total_time'] = (new_row['end_time'] - new_row['start_time'])
            # record test number
            new_row['test_number'] = i
            # decrement counter
            i += 1
            # print result
            print("%s on attempt %d took %d \t cyphertext is %s"%(selected_algo, i, new_row['total_time'], new_row['cypher_text']))
            # print("%s \n"%new_row)
###############
process_telemetry(device_profile())


###############
# send data
    # device tests table
        # row
            # test row id
            # sensor output speed
            # device name
            # device processor
            # device type
            # (start time - end time)
# receive success response
# re-run 1000 times
# take average time of all encryption events
# save average time to test result database
    # device tests table
        # row
            # test average row id
            # sensor output speed
            # device name
            # device type
            # successfully recorded test completions
            # average time
###############