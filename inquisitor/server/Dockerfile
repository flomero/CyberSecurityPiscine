FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
	vsftpd \
	net-tools \
	&& rm -rf /var/lib/apt/lists/*

COPY setup.sh /app/setup.sh
COPY vsftpd.conf /etc/vsftpd/vsftpd.conf

RUN mkdir -p /var/run/vsftpd/empty

CMD ["bash", "/app/setup.sh"]
