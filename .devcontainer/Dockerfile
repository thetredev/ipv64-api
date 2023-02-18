FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim-2023-02-13

ENV DEBIAN_FRONTEND=noninteractive

# Install git & vim
RUN apt-get update && \
    apt-get install -y --no-install-recommends git vim && \
    apt-get clean

# Add user 'vscode'
RUN groupadd -rg 1000 vscode && \
    useradd -rms /bin/bash -d /home/vscode -u 1000 -g vscode vscode

# Default to user 'vscode'
USER vscode

# Install Python module 'requests'
RUN pip3 install --user requests==2.28.2
