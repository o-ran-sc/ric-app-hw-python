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
# ==================================================================================

import json
from os import getenv
from ricxappframe.xapp_frame import RMRXapp, rmr
from ricxappframe.alarm import alarm


# pylint: disable=invalid-name
rmr_xapp = None


def post_init(self):
    """
    Function that runs when xapp initialization is complete
    """
    self.logger.info("post_init called")

def handle_config_change(self, config):
    """
    Function that runs at start and on every configuration file change.
    """
    self.logger.info("handle_config_change: config: {}".format(config))


def default_handler(self, summary, sbuf):
    """
    Function that processes messages for which no handler is defined
    """
    self.logger.info("default_handler called")
    self.rmr_free(sbuf)


def start(thread=False):
    """
    This is a convenience function that allows this xapp to run in Docker
    for "real" (no thread, real SDL), but also easily modified for unit testing
    (e.g., use_fake_sdl). The defaults for this function are for the Dockerized xapp.
    """
    global rmr_xapp
    fake_sdl = getenv("USE_FAKE_SDL", True)
    config_file = getenv("CONFIG_FILE", None)
    rmr_xapp = RMRXapp(default_handler,
                       config_handler=handle_config_change,
                       rmr_port=4560,
                       post_init=post_init,
                       use_fake_sdl=bool(fake_sdl))
    rmr_xapp.run(thread)


def stop():
    """
    can only be called if thread=True when started
    TODO: could we register a signal handler for Docker SIGTERM that calls this?
    """
    rmr_xapp.stop()

if __name__ == "__main__":
    start()
