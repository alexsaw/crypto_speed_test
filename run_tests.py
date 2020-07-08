import os
import time
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

###############
# process sensor telemetry (encrypt and send to database)
def tests(device_details, encryption_function):
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
            new_row['start_time'] = int(round(time.time() * 10000000))
            # encrypt the data
            new_row['cypher_text'] = encryption_function(algorithm_with_key)
            # connect to database
            # record end time
            new_row['end_time'] = int(round(time.time() * 10000000))
            # subtract end from start time
            new_row['total_time'] = (new_row['end_time'] - new_row['start_time'])
            # record test number
            new_row['test_number'] = i
            # decrement counter
            i += 1
            # print result
            print("%s on attempt %d took %d"%(selected_algo, i, new_row['total_time']))
            # print("%s \n"%new_row)
###############
#process_telemetry(device_profile())