# IPv64.net API Proxy Implementation (PoC)

This project aims to be a proof of concept proxy implementation of the [IPv64.net API](https://ipv64.net/api.php). The implementation is written in [Python 3.11](https://www.python.org) with the help of [FastAPI](https://fastapi.tiangolo.com).

**Note**: Only the API part is implemented/proxied, not the Updater part.

## The code

Have a look at the [poc/api.py](./poc/api.py) file.

## Why "proxy implementation"?

The IPv64.net API is neither [OpenAPI](https://www.openapis.org) compliant, nor is it documented in a developer-friendly way. This PoC is just a concept of how you could communicate with it and how the API calls actually work on a technical level.

## Setting up a local development environment

All you need is an editor with Python installed (minimum: 3.9, preferred: 3.11) and the following PIP packages:
- [`requests==2.28.2`](https://pypi.org/project/requests/2.28.2)
- [`fastapi==0.92.0`](https://pypi.org/project/fastapi/0.92.0)
- [`uvicorn==0.20.0`](https://pypi.org/project/uvicorn/0.20.0)

To run the dev server, execute the following command (works on both Linux and Windows):
```
uvicorn poc.api:api --reload
```

For Linux I created a helper script `dev-server.sh` which does the same thing.

## Or: Use a VS Code dev container (Linux only)

Open the project in [VS Code](https://code.visualstudio.com), install the extension [`Dev Containers`](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers), and execute `Dev Containers: Reopen in Container` from the command pallet.

**Note**: If your UID/GID pair is NOT `1000:1000`, make sure to update the [`Dockerfile`](./.devcontainer/Dockerfile) accordingly:

Change
```Dockerfile
# Add user 'vscode'
RUN groupadd -rg 1000 vscode && \
    useradd -rms /bin/bash -d /home/vscode -u 1000 -g vscode vscode
```

to
```Dockerfile
# Add user 'vscode'
RUN groupadd -rg <YOUR GID> vscode && \
    useradd -rms /bin/bash -d /home/vscode -u <YOUR UID> -g vscode vscode
```

## OpenAPI UI

Head over to http://localhost:8000/docs after you've run the server to test it.
