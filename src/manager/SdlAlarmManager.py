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
from ricxappframe.alarm import alarm
from ._BaseManager import _BaseManager


# noinspection PyProtectedMember,PyProtectedMember
class SdlAlarmManager(_BaseManager):

    def __init__(self, rmr_xapp: RMRXapp):
        super().__init__(rmr_xapp)
        self.alarm_mgr = alarm.AlarmManager(self._rmr_xapp._mrc, "ric-xapp", "hw-python")
        self.alarm_sdl = None

    def checkSdl(self):
        if self._rmr_xapp._sdl.healthcheck():
            # healthy, so clear the alarm if it was raised
            if self.alarm_sdl:
                self.logger.info("SdlAlarmManager:: clearing alarm")
                self.alarm_mgr.clear_alarm(self.alarm_sdl)
                self.alarm_sdl = None
        else:
            # not healthy, so (re-)raise the alarm
            self.logger.info("SdlAlarmManager:: connection to SDL is not healthy, raising alarm")
            if self.alarm_sdl:
                self.alarm_mgr.reraise_alarm(self.alarm_sdl)
            else:
                self.alarm_sdl = self.alarm_mgr.create_alarm(1, alarm.AlarmSeverity.CRITICAL,
                                                             "SdlAlarmManager:: SDL failure")
                self.alarm_mgr.raise_alarm(self.alarm_sdl)
            self.logger.warning("SdlAlarmManager:: dropping request!")
