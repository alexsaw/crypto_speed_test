################################
# This program simulates an IOT that collects data from a connected sensor and sends the data in an encrypted format to another device. it usees the cryptogrpahy library heavily: https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/#

# there are a number of dependencies which must be installed for this to work on your machine. they can be installed with the "pip install ____" command, where the placeholder there is the name of the library. The libraries needed are: platform, uuid, cryptography, os, and time

# we may need to compile this python into an executable for it to work on some of the other devices like cell phones we talked about
################################


# file dependencies (these are the other python files which must be located in the same directory -- here the functions in those files are being imported as variables to be brought in as arguments for the "tests()" function)
from device_profile import get_profile
from symmetric_encryption import encrypt
from run_tests import tests
# /file dependencies

# this is the function that runs everything else. use it by running "python main.py on linux, or python .\main.py in windows"
tests(get_profile, encrypt)