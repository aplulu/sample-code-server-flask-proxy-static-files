FROM codercom/code-server:latest

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 python3-pip python3.11-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER coder

EXPOSE 8080
