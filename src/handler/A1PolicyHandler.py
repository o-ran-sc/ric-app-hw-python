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
from ._BaseHandler import _BaseHandler


class A1PolicyHandler(_BaseHandler):

    def __init__(self, rmr_xapp: RMRXapp, msgtype):
        super().__init__(rmr_xapp, msgtype)

    def request_handler(self, rmr_xapp, summary, sbuf):
        self._rmr_xapp.rmr_free(sbuf)
        try:
            req = json.loads(summary[rmr.RMR_MS_PAYLOAD])  # input should be a json encoded as bytes
            self.logger.debug("A1PolicyHandler.resp_handler:: Handler processing request")
        except (json.decoder.JSONDecodeError, KeyError):
            self.logger.error("A1PolicyManager.resp_handler:: Handler failed to parse request")
            return

        if self.verifyPolicy(req):
            self.logger.info("A1PolicyHandler.resp_handler:: Handler processed request: {}".format(req))
        else:
            self.logger.error("A1PolicyHandler.resp_handler:: Request verification failed: {}".format(req))
            return
        self.logger.debug("A1PolicyHandler.resp_handler:: Request verification success: {}".format(req))

        resp = self.buildPolicyResp(req)
        self._rmr_xapp.rmr_send(json.dumps(resp).encode(), Constants.A1_POLICY_RESP)
        self.logger.info("A1PolicyHandler.resp_handler:: Response sent: {}".format(resp))

    def verifyPolicy(self, req: dict):
        for i in ["policy_type_id", "operation", "policy_instance_id"]:
            if i not in req:
                return False
        return True

    def buildPolicyResp(self, req: dict):
        req["handler_id"] = self._rmr_xapp.config["xapp_name"]
        del req["operation"]
        req["status"] = "OK"
        return req
