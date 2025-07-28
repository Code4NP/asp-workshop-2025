FROM ubuntu:24.04

RUN mkdir /usr/bin/micro
ENV MAMBA_ROOT_PREFIX=/usr/bin/micro

RUN apt-get update && \
    apt-get install -y wget curl && \
    rm -rf /var/lib/apt/lists/*

# Install code-server
RUN curl -fsSL https://code-server.dev/install.sh | sh &&\
    code-server --install-extension ms-python.python && \
    code-server --install-extension ms-toolsai.jupyter && \
    code-server --install-extension ms-toolsai.vscode-jupyter-cell-tags 


# Install Pixi and create dev environment
COPY pixi.toml /home/env/pixi.toml
RUN curl -Ls https://github.com/prefix-dev/pixi/releases/download/v0.30.0/pixi-x86_64-unknown-linux-musl -o /usr/local/bin/pixi &&\
    chmod +x /usr/local/bin/pixi && \
    pixi install --manifest-path /home/env/pixi.toml && \
    pixi clean cache -y

COPY . /home/workshop
RUN rm -rf /home/workshop/.git 