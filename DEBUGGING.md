# Developing in Cluster

e.g. fastcs-example

# Deploy the develop mode chart

First deploy the developer mode helm chart:
- checkout a branch 'develop'
- Switch the container to develop mode with developMode: true
- push the change
- ec deploy bl47p-ea-fastcs-01 develop

This will deploy the container running sleep and with a new PVC called bl47p-ea-fastcs-01-develop, containing:
- /workspaces mounted at /workspaces in the container
- /venv mounted at /venv in the container
- both mounts above will have the original container contents copied in by an init-container


# Get the process started with debugpy

Exec this in the container

```bash
python -Xfrozen_modules=off -m debugpy --listen 0.0.0.0:5678 --configure-subProcess true -m fastcs_example run /epics/ioc/config/controller.yaml
```

add `--wait-for-client` to debugpy to try debugging startup.

Port forward the debug port on your workstation

```bash
k port-forward -n p47-beamline bl47p-ea-fastcs-01-0 5678
```

# Get VSCode connected

mount the ...-develop PVC on your workstation and open it with vscode

```bash
pv-mounter mount p47-beamline bl47p-ea-fastcs-01-develop ./debugger
code debugger/workspaces/fastcs-example
```

Launch remote debugging with a launcher configuration like this:
```json
        {
            "name": "Python Debugger: Remote Attach",
            "type": "debugpy",
            "request": "attach",
            "connect": {
                "host": "localhost",
                "port": 5678
            },
            "pathMappings": [
                {
                    "localRoot": "${workspaceFolder}",
                    "remoteRoot": "."
                }
            ],
            "justMyCode": false
        },
```
