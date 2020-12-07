# ==================================================================================
#
#       Copyright (c) 2020 Samsung Electronics Co., Ltd. All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#          http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ==================================================================================


# This initialization script reads in a json from the specified config map path
# to set up the initializations (route config map, variables etc) for the main
# xapp process

import json
import sys
import os
import signal
import time

default_routing_file = "/opt/route/test_route.rt"
lport = 0


def signal_handler(signum, frame):
    print("Received signal {0}\n".format(signum))
    if xapp_subprocess is None or xapp_pid is None:
        print("No xapp running. Quiting without sending signal to xapp\n", flush=True)
    else:
        print("Sending signal {0} to xapp ...".format(signum), flush=True)
        xapp_subprocess.send_signal(signum)


def parseConfigJson(config):
    for k1 in config.keys():
        if k1 in ParseSection:
            result = ParseSection[k1](config)
            if not result:
                return False


def getMessagingInfo(config):
    global lport
    if 'messaging' in config.keys() and 'ports' in config['messaging'].keys():
        port_list = config['messaging']['ports']
        for portdesc in port_list:
            if 'port' in portdesc.keys() and 'name' in portdesc.keys() and portdesc['name'] == 'rmr-data':
                lport = portdesc['port']
                # Set the environment variable
                os.environ["HW_PORT"] = str(lport)
                return True
    if lport == 0:
        print("Error! No valid listening port", flush=True)
        return False


def getXappName(config):
    myKey = "xapp_name"
    if myKey not in config.keys():
        print(("Error ! No information found for {0} in config\n".format(myKey)), flush=True)
        return False

    xapp_name = config[myKey]
    print("Xapp Name is: " + xapp_name)
    os.environ["XAPP_NAME"] = xapp_name


ParseSection = dict()
ParseSection["xapp_name"] = getXappName
ParseSection["messaging"] = getMessagingInfo

# ================================================================
if __name__ == "__main__":

    import subprocess

    cmd = ["/usr/local/bin/run-hw-python.py"]
    config_file = os.getenv("CONFIG_FILE", None)

    if config_file is None:
        print("Error! No configuration file specified\n", flush=True)
        sys.exit(1)

    with open(config_file, 'r') as f:
        try:
            config = json.load(f)
        except Exception as e:
            print(("Error loading json file from {0}. Reason = {1}\n".format(config_file, e)), flush=True)
            sys.exit(1)

    result = parseConfigJson(config)
    if not result:
        print("Error parsing config json. Not executing xAPP", flush=True)
        sys.exit(1)

    else:

        print("Config read successfully", flush=True)

        # Register signal handlers
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)

        # Start the xAPP
        print("Executing xAPP ....", flush=True)
        xapp_subprocess = subprocess.Popen(cmd, shell=False, stdin=None, stdout=None, stderr=None)
        xapp_pid = xapp_subprocess.pid

        # Periodically poll the process every 5 seconds to check if still alive
        while 1:
            xapp_status = xapp_subprocess.poll()
            if xapp_status is None:
                time.sleep(5)
            else:
                print("XaPP terminated via signal {0}\n".format(-1 * xapp_status), flush=True)
                break
