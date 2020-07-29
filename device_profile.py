# dependencies
import platform
from uuid import getnode as get_mac
# /dependencies

###############
# identify the device this is running on
def get_profile():
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
