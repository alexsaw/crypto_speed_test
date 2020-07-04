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
    device_json = json.dumps(device_data, indent=4, sort_keys=False)
    # function returns a JSON object that describes the device this script is being run on
    return device_json
###############
print(device_profile())


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
    # symmetric key setup
    key = os.urandom(32)
    iv = os.urandom(16)
    algorithm = algorithms.AES(key)
    mode_of_operation = modes.CBC(iv)
    # generate symmetric cipher (I want to make this cycle through a few encryption types and cipher modes)
    cipher = Cipher(algorithm, mode_of_operation, backend=backend)
    encryptor = cipher.encryptor() 
    plain_text = b"a secret message"
    cipher_text = encryptor.update(plain_text) + encryptor.finalize()
    # test decryption of the 
    decryptor = cipher.decryptor()
    decrypted_plain_text = decryptor.update(cipher_text) + decryptor.finalize()
    print(decrypted_plain_text)
    # start sending encrypted data via process_telemtry() function
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
# process sensor telemetry (encrypt and send to database)
def process_telemetry(simulator_output, device_details):
    # record start time
    start_time = int(round(time.time() * 1000))
    # bring in random data to simulate data ingested by a connected sensor
    # encrypt the data
    # connect to database
    # record end time
    end_time = int(round(time.time() * 1000))
    print(end_time)
    # subtract end from start time
    total_time = end_time = start_time
###############
#process_telemetry(x,y)


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