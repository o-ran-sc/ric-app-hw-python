# O-RAN-SC Hello World Xapp in Python

This repository contains open-source code for a prototype python xAPP for near real-time
RAN Intelligent Controller which makes use of python Xapp Framework.

This xAPP aims to provide basic implementation of :

1. A1 interfaces interactions

2. Read-write operations into a persistent storage. 

3. xAPP Configuration management

4. RMR Health Check

5. xAPP SDL Check

6. Raising alarms

7. Generating metrics (TBD)

8. E2 Interface intereactions (TBD)


Introduction
------------

This document provides guidelines on how to install and configure the HW Python xAPP in various environments/operating modes.
The audience of this document is assumed to have good knowledge in RIC Platform.


Preface
-------
This xAPP can be run directly as a Linux binary, as a docker image, or in a pod in a Kubernetes environment.  The first
two can be used for dev testing. The last option is how an xAPP is deployed in the RAN Intelligent Controller environment.
This covers all three methods. 

1. Docker 

2. Linux Binary

3. Kubernetes 





##Build Process

The HW xAPP can be either tested as a Linux binary or as a docker image.
   1. **Linux binary**: The HW xAPP may be compiled and invoked directly.
      Pre-requisite software packages that must be installed prior to 
      compiling are documented in the Dockerfile in the repository.
      

   2. **Docker Image**:For building docker images, the Docker environment 
      must be present in the system.
      
      Change to the root of the repository   
      ```
      $ docker --no-cache build -t hw-python ./
      Sending build context to Docker daemon  439.3kB
      Step 1/18 : FROM python:3.8-alpine
      3.8-alpine: Pulling from library/python
      .
      .
      .
      .
      
      Step 17/18 : ENV DBAAS_SERVICE_HOST=service-ricplt-dbaas-tcp.ricplt.svc.cluster.local
       ---> Running in d00e08612ff4
      Removing intermediate container d00e08612ff4
       ---> da54555174d1
      Step 18/18 : CMD run-hw-python.py
       ---> Running in f96da2ac3f43
      Removing intermediate container f96da2ac3f43
       ---> 1b96cc7da63c
      Successfully built 1b96cc7da63c
      Successfully tagged hw-python:latest

      ```

      After the docker image is Successfully built , 
      Now run the hw-python:latest by following command:
      ```
      
      $ docker run hw-python:latest
      1625730731 1/RMR [INFO] sends: ts=1625730731 src=fdbb898edc12:4560 target=service-ricplt-a1mediator-rmr.ricplt:4562 open=0 succ=0 fail=0 (hard=0 soft=0)
      1625730731 1/RMR [INFO] sends: ts=1625730731 src=fdbb898edc12:4560 target=127.0.0.1:4560 open=0 succ=0 fail=0 (hard=0 soft=0)
      1625730762 1/RMR [INFO] sends: ts=1625730762 src=fdbb898edc12:4560 target=service-ricplt-a1mediator-rmr.ricplt:4562 open=0 succ=0 fail=0 (hard=0 soft=0)
      1625730762 1/RMR [INFO] sends: ts=1625730762 src=fdbb898edc12:4560 target=127.0.0.1:4560 open=0 succ=0 fail=0 (hard=0 soft=0)

      ```
      
Software Installation and Deployment
------------------------------------
### Onboarding of hw-python using dms_cli tool

`dms_cli` offers rich set of command line utility to onboard `hw-python` xapp
to `chartmuseme`.

First checkout the [hw-python](https://gerrit.o-ran-sc.org/r/ric-app/hw-python) repository from gerrit.

```
git clone "https://gerrit.o-ran-sc.org/r/ric-app/hw-python"
```

`hw-python` has following folder structure
```
+---docs
|           
+---hw_python.egg-info
|       
+---init
|       config-file.json # descriptor for xapp deployment.
|       init_script.py
|       test_route.rt
|       schema.json #schema for validating the config-file.json
|       
+---releases
|       
+---resources
|       
+---src

```

For onboarding `hw-python` make sure that `dms_cli` and helm3 is installed. One can follow [documentation](https://docs.o-ran-sc.org/projects/o-ran-sc-it-dep/en/latest/installation-guides.html#ric-applications) to
configure `dms_cli`.

Once `dms_cli` is availabe we can proceed to onboarding proceure.

configure the `export CHART_REPO_URL` to point `chartmuseme`.
```
$export CHART_REPO_URL=http://<service-ricplt-xapp-onboarder-http.ricplt>:8080
``` 

check if `dms_cli` working fine.
```
$ dms_cli health
True
```

Now move to `init` folder to initiate onboarding.

```
$ cd init

$ dms_cli onboard --config_file_path=config-file.json --shcema_file_path=schema.json
httpGet:
  path: '{{ index .Values "readinessProbe" "httpGet" "path" | toJson }}'
  port: '{{ index .Values "readinessProbe" "httpGet" "port" | toJson }}'
initialDelaySeconds: '{{ index .Values "readinessProbe" "initialDelaySeconds" | toJson }}'
periodSeconds: '{{ index .Values "readinessProbe" "periodSeconds" | toJson }}'

httpGet:
  path: '{{ index .Values "livenessProbe" "httpGet" "path" | toJson }}'
  port: '{{ index .Values "livenessProbe" "httpGet" "port" | toJson }}'
initialDelaySeconds: '{{ index .Values "livenessProbe" "initialDelaySeconds" | toJson }}'
periodSeconds: '{{ index .Values "livenessProbe" "periodSeconds" | toJson }}'

{
    "status": "Created"
}
```

Check if `hw-python` is onborded
```
$ curl --location --request GET "http://<appmgr>:32080/onboard/api/v1/charts"  --header 'Content-Type: application/json'
{
    "hw-python": [
        {
            "name": "hw-python",
            "version": "1.0.0",
            "description": "Standard xApp Helm Chart",
            "apiVersion": "v1",
            "appVersion": "1.0",
            "urls": [
                "charts/hw-python-1.0.0.tgz"
            ],
            "created": "2021-07-05T15:07:34.518377486Z",
            "digest": "e9db874d35154643a2c6f26dd52929c9dcf143f165683c03d07518bb0c2d768d"
        }
    ],
    "hw-python": [
        {
            "name": "hw-python",
            "version": "1.0.0",
            "description": "Standard xApp Helm Chart",
            "apiVersion": "v1",
            "appVersion": "1.0",
            "urls": [
                "charts/hw-python-1.0.0.tgz"
            ],
            "created": "2021-07-05T15:20:13.965653743Z",
            "digest": "975b1da1f8669e8ed1b1e5be809e7cf4841ef33abcb88207bc3a735e9b543a9a"
        }
    ]
}
```

If we would wish to download the charts then we can perform following curl operation :

```
curl --location --request GET "http://<appmgr>:32080/onboard/api/v1/charts/xapp/hw-python/ver/1.0.0"  --header 'Content-Type: application/json' --output hw-python.tgz
```
The downloaded folder has the deployment files for hw-python 
```
tar -xvzf hw-python.tgz
hw-python/Chart.yaml
hw-python/values.yaml
hw-python/templates/_helpers.tpl
hw-python/templates/appconfig.yaml
hw-python/templates/appenv.yaml
hw-python/templates/deployment.yaml
hw-python/templates/service-http.yaml
hw-python/templates/service-rmr.yaml
hw-python/config/config-file.json
hw-python/descriptors/schema.json

```

Now the onboarding is done.

### Deployment of hw-python 

Once charts are available we can deploy the the `hw-python` using following curl command :

```
$ curl --location --request POST "http://<appmgr>:32080/appmgr/ric/v1/xapps"  --header 'Content-Type: application/json'  --data-raw '{"xappName": "hw-python", "helmVersion": "1.0.0"}'
{"instances":null,"name":"hw-python","status":"deployed","version":"1.0"}
```

Deployment will be done in `ricxapp` ns :

```
# kubectl get pods -n ricxapp
NAME                                 READY   STATUS    RESTARTS   AGE
ricxapp-hw-python-64b5447dcc-mbt5w   1/1     Running   0          5m45s

       CLUSTER-IP       EXTERNAL-IP   PORT(S)             AGE
aux-entry                        ClusterIP   10.111.35.76     <none>        80/TCP,443/TCP      9d
service-ricxapp-hw-python-http   ClusterIP   10.104.223.245   <none>        8080/TCP            6m23s
service-ricxapp-hw-python-rmr    ClusterIP   10.103.243.21    <none>        4560/TCP,4561/TCP   6m23s

```

Now we can query to appmgr to get list of all the deployed xapps :

```
# curl http://service-ricplt-appmgr-http.ricplt:8080/ric/v1/xapps | jq .
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   347  100   347    0     0    578      0 --:--:-- --:--:-- --:--:--   579
[
  {
    "instances": [
      {
        "ip": "service-ricxapp-hw-python-rmr.ricxapp",
        "name": "hw-python-55ff7549df-kpj6k",
        "policies": [
          1
        ],
        "port": 4560,
        "rxMessages": [
          "RIC_SUB_RESP",
          "A1_POLICY_REQ",
          "RIC_HEALTH_CHECK_REQ"
        ],
        "status": "running",
        "txMessages": [
          "RIC_SUB_REQ",
          "A1_POLICY_RESP",
          "A1_POLICY_QUERY",
          "RIC_HEALTH_CHECK_RESP"
        ]
      }
    ],
    "name": "hw-python",
    "status": "deployed",
    "version": "1.0"
  }
]

```
Logs from `hw-python` :

```
# kubectl  logs ricxapp-hw-python-55ff7549df-kpj6k -n ricxapp
{"ts":1624562552123,"crit":"INFO","id":"hw-app","mdc":{"time":"2021-06-24T19:22:32"},"msg":"Using config file: config/config-file.json"}
{"ts":1624562552124,"crit":"INFO","id":"hw-app","mdc":{"CONTAINER_NAME":"","HOST_NAME":"","PID":"6","POD_NAME":"","SERVICE_NAME":"","SYSTEM_NAME":"","time":"2021-06-24T19:22:32"},"msg":"Serving metrics on: url=/ric/v1/metrics namespace=ricxapp"}
{"ts":1624562552133,"crit":"INFO","id":"hw-app","mdc":{"CONTAINER_NAME":"","HOST_NAME":"","PID":"6","POD_NAME":"","SERVICE_NAME":"","SYSTEM_NAME":"","time":"2021-06-24T19:22:32"},"msg":"Register new counter with opts: {ricxapp SDL Stored The total number of stored SDL transactions map[]}"}
{"ts":1624562552133,"crit":"INFO","id":"hw-app","mdc":{"CONTAINER_NAME":"","HOST_NAME":"","PID":"6","POD_NAME":"","SERVICE_NAME":"","SYSTEM_NAME":"","time":"2021-06-24T19:22:32"},"msg":"Register new counter with opts: {ricxapp SDL StoreError The total number of SDL store errors map[]}"}
1624562552 6/RMR [INFO] ric message routing library on SI95 p=0 mv=3 flg=00 (fd4477a 4.5.2 built: Jan 21 2021)
{"ts":1624562552140,"crit":"INFO","id":"hw-app","mdc":{"CONTAINER_NAME":"","HOST_NAME":"","HWApp":"0.0.1","PID":"6","POD_NAME":"","SERVICE_NAME":"","SYSTEM_NAME":"","time":"2021-06-24T19:22:32"},"msg":"new rmrClient with parameters: ProtPort=0 MaxSize=0 ThreadType=0 StatDesc=RMR LowLatency=false FastAck=false Policies=[]"}
{"ts":1624562552140,"crit":"INFO","id":"hw-app","mdc":{"CONTAINER_NAME":"","HOST_NAME":"","HWApp":"0.0.1","PID":"6","POD_NAME":"","SERVICE_NAME":"","SYSTEM_NAME":"","time":"2021-06-24T19:22:32"},"msg":"Register new counter with opts: {ricxapp RMR Transmitted The total number of transmited RMR messages map[]}"}
{"ts":1624562552140,"crit":"INFO","id":"hw-app","mdc":{"CONTAINER_NAME":"","HOST_NAME":"","HWApp":"0.0.1","PID":"6","POD_NAME":"","SERVICE_NAME":"","SYSTEM_NAME":"","time":"2021-06-24T19:22:32"},"msg":"Register new counter with opts: {ricxapp RMR Received The total number of received RMR messages map[]}"}
{"ts":1624562552140,"crit":"INFO","id":"hw-app","mdc":{"CONTAINER_NAME":"","HOST_NAME":"","HWApp":"0.0.1","PID":"6","POD_NAME":"","SERVICE_NAME":"","SYSTEM_NAME":"","time":"2021-06-24T19:22:32"},"msg":"Register new counter with opts: {ricxapp RMR TransmitError The total number of RMR transmission errors map[]}"}
{"ts":1624562552140,"crit":"INFO","id":"hw-app","mdc":{"CONTAINER_NAME":"","HOST_NAME":"","HWApp":"0.0.1","PID":"6","POD_NAME":"","SERVICE_NAME":"","SYSTEM_NAME":"","time":"2021-06-24T19:22:32"},"msg":"Register new counter with opts: {ricxapp RMR ReceiveError The total number of RMR receive errors map[]}"}
{"ts":1624562552140,"crit":"INFO","id":"hw-app","mdc":{"CONTAINER_NAME":"","HOST_NAME":"","HWApp":"0.0.1","PID":"6","POD_NAME":"","SERVICE_NAME":"","SYSTEM_NAME":"","time":"2021-06-24T19:22:32"},"msg":"Xapp started, listening on: :8080"}
{"ts":1624562552140,"crit":"INFO","id":"hw-app","mdc":{"CONTAINER_NAME":"","HOST_NAME":"","HWApp":"0.0.1","PID":"6","POD_NAME":"","SERVICE_NAME":"","SYSTEM_NAME":"","time":"2021-06-24T19:22:32"},"msg":"rmrClient: Waiting for RMR to be ready ..."}
{"ts":1624562553140,"crit":"INFO","id":"hw-app","mdc":{"CONTAINER_NAME":"","HOST_NAME":"","HWApp":"0.0.1","PID":"6","POD_NAME":"","SERVICE_NAME":"","SYSTEM_NAME":"","time":"2021-06-24T19:22:33"},"msg":"rmrClient: RMR is ready after 1 seconds waiting..."}
{"ts":1624562553141,"crit":"INFO","id":"hw-app","mdc":{"CONTAINER_NAME":"","HOST_NAME":"","HWApp":"0.0.1","PID":"6","POD_NAME":"","SERVICE_NAME":"","SYSTEM_NAME":"","time":"2021-06-24T19:22:33"},"msg":"xApp ready call back received"}
1624562553 6/RMR [INFO] sends: ts=1624562553 src=service-ricxapp-hw-python-rmr.ricxapp:0 target=localhost:4591 open=0 succ=0 fail=0 (hard=0 soft=0)
1624562553 6/RMR [INFO] sends: ts=1624562553 src=service-ricxapp-hw-python-rmr.ricxapp:0 target=localhost:4560 open=0 succ=0 fail=0 (hard=0 soft=0)
1624562553 6/RMR [INFO] sends: ts=1624562553 src=service-ricxapp-hw-python-rmr.ricxapp:0 target=service-ricplt-a1mediator-rmr.ricplt:4562 open=0 succ=0 fail=0 (hard=0 soft=0)
RMR is ready now ...
{"ts":1624562557140,"crit":"INFO","id":"hw-app","mdc":{"CONTAINER_NAME":"","HOST_NAME":"","HWApp":"0.0.1","PID":"6","POD_NAME":"","SERVICE_NAME":"","SYSTEM_NAME":"","time":"2021-06-24T19:22:37"},"msg":"Application='hw-python' is not ready yet, waiting ..."}
{"ts":1624562562141,"crit":"INFO","id":"hw-app","mdc":{"CONTAINER_NAME":"","HOST_NAME":"","HWApp":"0.0.1","PID":"6","POD_NAME":"","SERVICE_NAME":"","SYSTEM_NAME":"","time":"2021-06-24T19:22:42"},"msg":"Application='hw-python' is not ready yet, waiting ..."}
{"ts":1624562567141,"crit":"INFO","id":"hw-app","mdc":{"CONTAINER_NAME":"","HOST_NAME":"","HWApp":"0.0.1","PID":"6","POD_NAME":"","SERVICE_NAME":"","SYSTEM_NAME":"","time":"2021-06-24T19:22:47"},"msg":"Application='hw-python' is not ready yet, waiting ..."}
{"ts":1624562567370,"crit":"INFO","id":"hw-app","mdc":{"CONTAINER_NAME":"","HOST_NAME":"","HWApp":"0.0.1","PID":"6","POD_NAME":"","SERVICE_NAME":"","SYSTEM_NAME":"","time":"2021-06-24T19:22:47"},"msg":"restapi: method=GET url=/ric/v1/health/ready"}
{"ts":1624562569766,"crit":"INFO","id":"hw-app","mdc":{"CONTAINER_NAME":"","HOST_NAME":"","HWApp":"0.0.1","PID":"6","POD_NAME":"","SERVICE_NAME":"","SYSTEM_NAME":"","time":"2021-06-24T19:22:49"},"msg":"restapi: method=GET url=/ric/v1/health/alive"}
```

Here we are done with the onboaring and deployment of `hw-python`.





Testing 
--------

Unit tests TBD


## License

```

   Copyright (c) 2020 Samsung Electronics Co., Ltd. All Rights Reserved.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

```
