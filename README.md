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
      
      Change to the the root of the repository   
      ```
      $ docker --no-cache build -t <image-name> ./
      Sending build context to Docker daemon  439.3kB
      Step 1/18 : FROM python:3.8-alpine
      3.8-alpine: Pulling from library/python
      5843afab3874: Already exists
      1174600ee52d: Already exists
      60b674152618: Pull complete
      9eb7372222dd: Pull complete
      57f80b42c60b: Pull complete
      Digest: sha256:697be30b0ef728b8ebc0e8fc38b561153545666f1262beac74468a94ffb44375
      Status: Downloaded newer image for python:3.8-alpine
       ---> 5e8816ee5207
      Step 2/18 : COPY --from=nexus3.o-ran-sc.org:10002/o-ran-sc/bldr-alpine3-rmr:4.0.5 /usr/local/lib64/librmr* /usr/local/lib64/
      4.0.5: Pulling from o-ran-sc/bldr-alpine3-rmr
      63656a819106: Pull complete
      7f5f6b9920dc: Pull complete
      503af471e686: Pull complete
      Digest: sha256:eb906735a7969bf0e341ba30c5087c84c393e283ae666edde423bb8f8ca0b24e
      Status: Downloaded newer image for nexus3.o-ran-sc.org:10002/o-ran-sc/bldr-alpine3-rmr:4.0.5
       ---> e26468a7dceb
      Step 3/18 : RUN mkdir -p /opt/route/
       ---> Running in 6ebd07606802
      Removing intermediate container 6ebd07606802
       ---> bbe349bea221
      Step 4/18 : COPY init/test_route.rt /opt/route/test_route.rt
       ---> 273f52fb04a3
      Step 5/18 : ENV LD_LIBRARY_PATH /usr/local/lib/:/usr/local/lib64
       ---> Running in 2f720b98d469
      Removing intermediate container 2f720b98d469
       ---> f65fea10ab70
      Step 6/18 : ENV RMR_SEED_RT /opt/route/test_route.rt
       ---> Running in b23e6f0e6dbf
      Removing intermediate container b23e6f0e6dbf
       ---> 7a02ac85d853
      Step 7/18 : RUN apk update && apk add gcc musl-dev bash
       ---> Running in fcecd4a72758
      fetch https://dl-cdn.alpinelinux.org/alpine/v3.14/main/x86_64/APKINDEX.tar.gz
      fetch https://dl-cdn.alpinelinux.org/alpine/v3.14/community/x86_64/APKINDEX.tar.gz
      v3.14.0-70-gd0f9887ff3 [https://dl-cdn.alpinelinux.org/alpine/v3.14/main]
      v3.14.0-101-ge32d6df770 [https://dl-cdn.alpinelinux.org/alpine/v3.14/community]
      OK: 14931 distinct packages available
      (1/13) Installing bash (5.1.4-r0)
      Executing bash-5.1.4-r0.post-install
      (2/13) Installing libgcc (10.3.1_git20210424-r2)
      (3/13) Installing libstdc++ (10.3.1_git20210424-r2)
      (4/13) Installing binutils (2.35.2-r2)
      (5/13) Installing libgomp (10.3.1_git20210424-r2)
      (6/13) Installing libatomic (10.3.1_git20210424-r2)
      (7/13) Installing libgphobos (10.3.1_git20210424-r2)
      (8/13) Installing gmp (6.2.1-r0)
      (9/13) Installing isl22 (0.22-r0)
      (10/13) Installing mpfr4 (4.1.0-r0)
      (11/13) Installing mpc1 (1.2.1-r0)
      (12/13) Installing gcc (10.3.1_git20210424-r2)
      (13/13) Installing musl-dev (1.2.2-r3)
      Executing busybox-1.33.1-r2.trigger
      OK: 134 MiB in 48 packages
      Removing intermediate container fcecd4a72758
       ---> a1d1c43632bb
      Step 8/18 : COPY setup.py /tmp
       ---> 60081d18d56d
      Step 9/18 : COPY README.md /tmp
       ---> 4520e077b34f
      Step 10/18 : COPY LICENSE.txt /tmp/
       ---> 75919e459642
      Step 11/18 : COPY src/ /tmp/src
       ---> e397eb4efa8c
      Step 12/18 : COPY init/ /tmp/init
       ---> e3437f9e403f
      Step 13/18 : RUN pip install /tmp
       ---> Running in 79d218c4785f
      Processing /tmp
        DEPRECATION: A future pip version will change local packages to be built in-place without first copying to a temporary directory. We recommend you use --use-feature=in-tree-build to test your packages with this new behavior before it becomes the default.
         pip 21.3 will remove support for this functionality. You can find discussion regarding this at https://github.com/pypa/pip/issues/7555.
      Collecting ricxappframe<2.0.0,>=1.1.1
        Downloading ricxappframe-1.6.0-py3-none-any.whl (39 kB)
      Collecting msgpack
        Downloading msgpack-1.0.2.tar.gz (123 kB)
      Collecting mdclogpy
        Downloading mdclogpy-1.1.4-py3-none-any.whl (6.5 kB)
      Collecting ricsdl<3.0.0,>=2.1.0
        Downloading ricsdl-2.3.0-py3-none-any.whl (34 kB)
      Collecting inotify-simple
        Downloading inotify_simple-1.3.5.tar.gz (9.7 kB)
      Requirement already satisfied: setuptools in /usr/local/lib/python3.8/site-packages (from ricsdl<3.0.0,>=2.1.0->ricxappframe<2.0.0,>=1.1.1->hw-python==0.0.1) (57.0.0)
      Collecting hiredis
        Downloading hiredis-2.0.0.tar.gz (75 kB)
      Collecting redis
        Downloading redis-3.5.3-py2.py3-none-any.whl (72 kB)
      Collecting inotify
        Downloading inotify-0.2.10.tar.gz (9.9 kB)
      Collecting nose
        Downloading nose-1.3.7-py3-none-any.whl (154 kB)
      Building wheels for collected packages: hw-python, hiredis, inotify-simple, inotify, msgpack
        Building wheel for hw-python (setup.py): started
        Building wheel for hw-python (setup.py): finished with status 'done'
        Created wheel for hw-python: filename=hw_python-0.0.1-py3-none-any.whl size=15557 sha256=dc9c0b34b3f040c9519ceaf6b57b995f49940b438cac07d9f5dbf1a2bf80f5d8
        Stored in directory: /tmp/pip-ephem-wheel-cache-lfvaalva/wheels/78/ab/a0/8496039e7645dd3b09b709a816d0511de18e2e54229b2543cc
        Building wheel for hiredis (setup.py): started
        Building wheel for hiredis (setup.py): finished with status 'done'
        Created wheel for hiredis: filename=hiredis-2.0.0-cp38-cp38-linux_x86_64.whl size=25524 sha256=34c3bac74bb6c0fc908d2b045346f766ffb340442e513409c1dfc9f49f992062
        Stored in directory: /root/.cache/pip/wheels/40/f9/92/4f916d7efad1897f2921f8694fa654619198da80ad6afc7996
        Building wheel for inotify-simple (setup.py): started
        Building wheel for inotify-simple (setup.py): finished with status 'done'
        Created wheel for inotify-simple: filename=inotify_simple-1.3.5-py3-none-any.whl size=7704 sha256=6371af0409c884e2d59b27f2e6e1c5073fada7278beb5aff9fbebff1cd304a15
        Stored in directory: /root/.cache/pip/wheels/85/b2/be/354e28439e9b15a9a77924041be045e499f11bb03493529246
        Building wheel for inotify (setup.py): started
        Building wheel for inotify (setup.py): finished with status 'done'
        Created wheel for inotify: filename=inotify-0.2.10-py3-none-any.whl size=13447 sha256=3808ebc545f389a2af65309d47469e86218ff3531ac138bab16b4bb443c2db72
        Stored in directory: /root/.cache/pip/wheels/aa/4f/40/336d4e7eafa5c72c2901f5999ba04a3186a0b4e52b035685b6
        Building wheel for msgpack (setup.py): started
        Building wheel for msgpack (setup.py): finished with status 'done'
        Created wheel for msgpack: filename=msgpack-1.0.2-cp38-cp38-linux_x86_64.whl size=15833 sha256=40f805c6aeca97f30bb3145d0fb85dbb80799212d7876b8723e1f36d67e01c75
        Stored in directory: /root/.cache/pip/wheels/80/54/1e/543cc300f5a40fbdda81274333957ba34e4f5cae40ed73317e
      Successfully built hw-python hiredis inotify-simple inotify msgpack
      Installing collected packages: nose, redis, inotify, hiredis, ricsdl, msgpack, mdclogpy, inotify-simple, ricxappframe, hw-python
      WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
      Successfully installed hiredis-2.0.0 hw-python-0.0.1 inotify-0.2.10 inotify-simple-1.3.5 mdclogpy-1.1.4 msgpack-1.0.2 nose-1.3.7 redis-3.5.3 ricsdl-2.3.0 ricxappframe-1.6.0
      Removing intermediate container 79d218c4785f
       ---> cb512123e930
      Step 14/18 : ENV PYTHONUNBUFFERED 1
       ---> Running in 18f5674d3950
      Removing intermediate container 18f5674d3950
       ---> 0cda98d4e22d
      Step 15/18 : ENV CONFIG_FILE=/tmp/init/config-file.json
       ---> Running in 47d2f8f81042
      Removing intermediate container 47d2f8f81042
       ---> 339a9c756097
      Step 16/18 : ENV DBAAS_SERVICE_PORT=6379
       ---> Running in d4ff616983c6
      Removing intermediate container d4ff616983c6
       ---> 1a571eafe1dc
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
|   |   conf.py
|   |   conf.yaml
|   |   favicon.ico
|   |   index.rst
|   |   installation-guide.rst
|   |   overview.rst
|   |   release-notes.rst
|   |   requirements-docs.txt
|   |   user-guide.rst
|   |   
|   \---_static
|           logo.png
|           
+---hw_python.egg-info
|       dependency_links.txt
|       entry_points.txt
|       PKG-INFO
|       requires.txt
|       SOURCES.txt
|       top_level.txt
|       
+---init
|       config-file.json
|       init_script.py
|       test_route.rt
|       
+---releases
|       container-release-ric-app-hw-python.yaml
|       
+---resources
|       pod.yaml
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
