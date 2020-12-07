import json
from ricxappframe.xapp_frame import RMRXapp, rmr
from .constants import constants


class A1PolicyManager():
    __rmr_xapp = None

    def __init__(self, rmr_xapp: RMRXapp):
        self.__rmr_xapp = rmr_xapp
        self.logger = self.__rmr_xapp.logger

    def startup(self):
        policy_query = "{\"policy_type_id\":" + str(constants.HELLOWORLD_POLICY_ID) + "}"
        self.__rmr_xapp.rmr_send(json.dumps(policy_query).encode(), constants.A1_POLICY_QUERY)
        self.logger.info("A1PolicyManager.startup:: Sent A1 policy query = " + policy_query)

    def resp_handler(self, summary, sbuf):
        self.__rmr_xapp.rmr_free(sbuf)
        try:
            req = json.loads(summary[rmr.RMR_MS_PAYLOAD])  # input should be a json encoded as bytes
            self.logger.debug("A1PolicyManager.resp_handler:: Handler processing request")
        except (json.decoder.JSONDecodeError, KeyError):
            self.logger.error("A1PolicyManager.resp_handler:: Handler failed to parse request: {}".format(req))
            return
        if self.verifyPolicy(req):
            self.logger.info("A1PolicyManager.resp_handler:: Handler processed request: {}".format(req))
        else:
            self.logger.error("A1PolicyManager.resp_handler:: Request verification failed: {}".format(req))
            return
        self.logger.debug("A1PolicyManager.resp_handler:: Request verification success: {}".format(req))

        resp = self.buildPolicyResp(req)
        self.__rmr_xapp.rmr_send(json.dumps(resp).encode(), constants.A1_POLICY_RESP)
        self.logger.info("A1PolicyManager.resp_handler:: Response sent: {}".format(resp))

    def verifyPolicy(self, req: dict):
        for i in ["policy_type_id", "operation", "policy_instance_id"]:
            if i not in req:
                return False
        return True

    def buildPolicyResp(self, req: dict):
        req["handler_id"] = self.config["xapp_name"]
        del req["operation"]
        req["policy_type_id"] = constants.A1_POLICY_RESP
        req["status"] = "OK"
        return req
