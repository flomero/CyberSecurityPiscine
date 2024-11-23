FROM python:3.10-slim

WORKDIR /app

# Install required tools
RUN apt-get update && apt-get install -y \
    tcpdump libpcap-dev iproute2 \
    && rm -rf /var/lib/apt/lists/*

    RUN apt-get clean

RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install --upgrade pip
RUN /opt/venv/bin/pip install \
    scapy \
    argparse \
    ipaddress \
    typing \
    colorama

ENV PATH="/opt/venv/bin:$PATH"

RUN echo "alias inquisitor='./inquisitor.py 10.10.0.102 00:00:00:00:00:02 10.10.0.103 00:00:00:00:00:03'" >> ~/.bashrc