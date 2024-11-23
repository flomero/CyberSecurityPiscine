FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
	ftp \
	net-tools \
	iputils-ping \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /app

CMD ["bash"]
