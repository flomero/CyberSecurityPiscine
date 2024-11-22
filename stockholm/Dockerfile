from ubuntu:latest

RUN apt-get update && apt-get install -y \
	python3 \
	python3-pip \
	python3-venv \
	curl

RUN apt-get clean

RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install --upgrade pip
RUN /opt/venv/bin/pip install argparse colorama cryptography

ENV PATH="/opt/venv/bin:$PATH"
