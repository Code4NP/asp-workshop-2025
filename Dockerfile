FROM ubuntu:24.04

RUN mkdir /usr/bin/micro
ENV MAMBA_ROOT_PREFIX=/usr/bin/micro

RUN apt-get update && apt-get install -y wget curl bzip2

RUN curl -Ls https://github.com/prefix-dev/pixi/releases/download/v0.30.0/pixi-x86_64-unknown-linux-musl -o /usr/local/bin/pixi
RUN chmod +x /usr/local/bin/pixi

# Install code-server
RUN curl -fsSL https://code-server.dev/install.sh | sh

RUN code-server --install-extension ms-python.python && \
    code-server --install-extension ms-toolsai.jupyter && \
    code-server --install-extension ms-toolsai.vscode-jupyter-cell-tags 
    
RUN  mkdir /home/workshop 

COPY pixi.toml /home/workshop/pixi.toml

RUN pixi install --manifest-path /home/workshop/pixi.toml  && \
    chown -R 1000:1000 /home/workshop


