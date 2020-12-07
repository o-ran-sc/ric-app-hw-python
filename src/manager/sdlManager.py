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

from ricxappframe.xapp_frame import RMRXapp
import json
from .baseManager import baseManager


class sdlManager(baseManager):

    __namespace = "e2Manager"

    def __init__(self, rmr_xapp: RMRXapp):
        super().__init__(rmr_xapp)

    def sdlGetGnbList(self):
        gnbList = self._rmr_xapp.sdl_find_and_get(ns=self.__namespace, prefix="GNB")
        self.logger.info("sdlManager.sdlGetGnbList:: Processed request: {}".format(json.dumps(gnbList)))

    def sdlGetEnbList(self):
        enbList = self._rmr_xapp.sdl_find_and_get(ns=self.__namespace, prefix="ENB")
        self.logger.info("sdlManager.sdlGetGnbList:: Handler processed request: {}".format(json.dumps(enbList)))




