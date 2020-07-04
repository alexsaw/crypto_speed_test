import cryptography
import platform
from uuid import getnode as get_mac
import json
import time

#
# This program simulates an IOT that collects data from a connected sensor and sends the data in an encrypted format to another device.
#

#
#
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

    device_json = json.dumps(device_data, indent=4, sort_keys=False)

    return device_json
#
#
#

#
#
# Deliver sensor events as quickly as you want to simulate a sensor event
def sensor_simulator(event_frequency):
    # every milisecond an event comes in
    if (event_frequency == 1):

    # every half second an event comes in
    elif (event_frequency == 2):

    # every second an event comes in
    elif (event_frequency == 3):

    # every 2 seconds an event comes in
    elif (event_frequency == 4):
#
#
#

#
#
# process sensor telemetry (encrypt and send to database)
def process_telemetry(simulator_output, device_details)
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
#
#
#

#
#
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
