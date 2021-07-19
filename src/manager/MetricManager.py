# ==================================================================================
#
#       Copyright (c) 2021 Samsung Electronics Co., Ltd. All Rights Reserved.
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
from ricxappframe.metric import metric
from ._BaseManager import _BaseManager
from datetime import datetime

# noinspection PyProtectedMember,PyProtectedMember
class MetricManager(_BaseManager):

    def __init__(self, rmr_xapp: RMRXapp):
        super().__init__(rmr_xapp)
        self.metric_mgr = metric.MetricsManager(self._rmr_xapp._mrc, "system-time", "hw-python")

    def send_metric(self):

        # datetime object containing current date and time
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        metric_list = [dt_string]
        self.logger.info("MetricManager:: metric time {}".format(metric_list))
        self.metric_mgr.send_metrics(metric_list)
        self.logger.info("MetricManager:: metric sent")

