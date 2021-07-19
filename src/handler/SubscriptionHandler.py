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
"""
Handles subscription messages from enbs and gnbs through rmr.
"""

import json
from ricxappframe.xapp_frame import RMRXapp, rmr
from ..utils.constants import Constants
from ._BaseHandler import _BaseHandler
from ..manager.SdlManager import SdlManager
class SubscriptionHandler(_BaseHandler):

    def __init__(self, rmr_xapp: RMRXapp, msgtype):
        super().__init__(rmr_xapp, msgtype)


    def request_handler(self, rmr_xapp, summary, sbuf):
        """
                Handles subscription messages.

                Parameters
                ----------
                rmr_xapp: rmr Instance Context

                summary: dict (required)
                    buffer content

                sbuf: str (required)
                    length of the message
        """
        self._rmr_xapp.rmr_free(sbuf)
        try:
            req = json.loads(summary[rmr.RMR_MS_PAYLOAD])  # input should be a json encoded as bytes
            self.logger.debug("SubscriptionHandler.resp_handler:: Handler processing request")
        except (json.decoder.JSONDecodeError, KeyError):
            self.logger.error("Subscription.resp_handler:: Handler failed to parse request")
            return

        if self.verifySubscription(req):
            self.logger.info("SubscriptionHandler.resp_handler:: Handler processed request: {}".format(req))
        else:
            self.logger.error("SubscriptionHandler.resp_handler:: Request verification failed: {}".format(req))
            return
        self.logger.debug("SubscriptionHandler.resp_handler:: Request verification success: {}".format(req))


    def verifySubscription(self, req: dict):
        for i in ["subscription_id", "message"]:
            if i not in req:
                return False
        return True










