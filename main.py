################################
# This program simulates an IOT that collects data from a connected sensor and sends the data in an encrypted format to another device. it usees the cryptogrpahy library heavily: https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/#
################################

# file dependencies
from device_profile import get_profile
from symmetric_encryption import encrypt
from run_tests import tests
# /file dependencies


tests(get_profile, encrypt)