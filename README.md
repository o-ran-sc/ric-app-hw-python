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



Software Installation and Deployment
------------------------------------
The build process assumes a Linux environment with python >= 3.8  and  has been tested on Ubuntu. For building docker images,
the Docker environment must be present in the system.


##Build Process

The HW xAPP can be either tested as a Linux binary or as a docker image.
   1. **Linux binary**: 
      TBD

   2. **Docker Image**: From the root of the repository, run   *docker --no-cache build -t <image-name> ./* .


##Deployment

**Invoking  xAPP docker container directly** (not in RIC Kubernetes env.):
        One can include the pod.yaml for including it in k8s build. Replace the image name with one built.
        TBD: Adding hw-python to nexus repo


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
