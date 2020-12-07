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

import json
from ricxappframe.xapp_frame import RMRXapp, rmr
from ..utils.constants import Constants
from ._BaseManager import _BaseManager


class A1PolicyManager(_BaseManager):

    def __init__(self, rmr_xapp: RMRXapp):
        super().__init__(rmr_xapp)

    def startup(self):
        policy_query = '{"policy_type_id":"' + str(Constants.HELLOWORLD_POLICY_ID) + '"}'
        self._rmr_xapp.rmr_send(policy_query.encode(), Constants.A1_POLICY_QUERY)
        self.logger.info("A1PolicyManager.startup:: Sent A1 policy query = " + policy_query)

