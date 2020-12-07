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

from os import getenv
from ricxappframe.xapp_frame import RMRXapp, rmr
from .utils.constants import Constants
from .manager import *
from .handler import *
from mdclogpy import Logger


class HWXapp:

    def __init__(self):
        fake_sdl = getenv("USE_FAKE_SDL", False)
        self.logger = Logger(name=__name__)
        self.rmr_xapp = RMRXapp(self._default_handler,
                                config_handler=self._handle_config_change,
                                rmr_port=4560,
                                post_init=self._post_init,
                                use_fake_sdl=bool(fake_sdl))

    def _post_init(self, rmr_xapp):
        """
        Function that runs when xapp initialization is complete
        Do note this function gets called before self.rmr_xapp is created
        """
        self.logger.info("HWXapp.post_init :: post_init called")
        # self.sdl_alarm_mgr = SdlAlarmManager()
        sdl_mgr = SdlManager(self)
        sdl_mgr.sdlGetGnbList()
        a1_mgr = A1PolicyManager(self)
        a1_mgr.startup()

    def _handle_config_change(self, _, config):
        """
        Function that runs at start and on every configuration file change.
        Do note this function gets called before self.rmr_xapp is created
        """
        self.logger.info("HWXapp.handle_config_change:: config: {}".format(config))
        self.config = config  # No mutex required due to GIL

    def _default_handler(self, rmr_xapp, summary, sbuf):
        """
        Function that processes messages for which no handler is defined
        """
        self.logger.info("HWXapp.default_handler called for msg type = " +
                                   str(summary[rmr.RMR_MS_MSG_TYPE]))
        self.rmr_xapp.rmr_free(sbuf)

    def _createHandlers(self):
        """
        Function that creates all the handlers for RMR Messages
        """
        HealthCheckHandler(self, Constants.RIC_HEALTH_CHECK_REQ)
        A1PolicyHandler(self, Constants.A1_POLICY_REQ)

    def start(self, thread=False):
        """
        This is a convenience function that allows this xapp to run in Docker
        for "real" (no thread, real SDL), but also easily modified for unit testing
        (e.g., use_fake_sdl). The defaults for this function are for the Dockerized xapp.
        """
        self._createHandlers()
        self.rmr_xapp.run(thread)

    def stop(self):
        """
        can only be called if thread=True when started
        TODO: could we register a signal handler for Docker SIGTERM that calls this?
        """
        self.rmr_xapp.stop()
