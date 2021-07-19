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

"""

import requests
from ricxappframe.xapp_frame import RMRXapp
import json
from ..utils.constants import Constants
from ._BaseManager import _BaseManager
from swagger_client import api_client

class SubscriptionManager(_BaseManager):

    __namespace = "e2Manager"

    def __init__(self, rmr_xapp: RMRXapp):
        super().__init__(rmr_xapp)
        _client = api_client()

    def get_gnb_list(self):
        gnblist = self._rmr_xapp.get_list_gnb_ids()   # yet to come in library
        self.logger.info("SubscriptionManager.getGnbList:: Processed request: {}".format(json.dumps(gnblist)))
        return gnblist

    def get_enb_list(self):
        enblist = self._rmr_xapp.get_list_enb_ids()   # yet to come in library
        self.logger.info("SubscriptionManager.sdlGetGnbList:: Handler processed request: {}".format(json.dumps(enblist)))
        return enblist

    def send_subscription_request(self,xnb_id):
        subscription_request = {"xnb_id": xnb_id, "action_type": Constants.ACTION_TYPE}
        try:
            json_object = json.dumps(subscription_request,indent=4)
        except TypeError:
            print("Unable to serialize the object")
        url = Constants.SUBSCRIPTION_PATH.format(Constants.PLT_NAMESPACE,
                                                 Constants.SUBSCRIPTION_SERVICE,
                                                 Constants.SUBSCRIPTION_PORT)
        try:
            response = requests.post(url , json=json_object)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err_h:
            return "An Http Error occurred:" + repr(err_h)
        except requests.exceptions.ConnectionError as err_c:
            return "An Error Connecting to the API occurred:" + repr(err_c)
        except requests.exceptions.Timeout as err_t:
            return "A Timeout Error occurred:" + repr(err_t)
        except requests.exceptions.RequestException as err:
            return "An Unknown Error occurred" + repr(err)







