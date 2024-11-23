FROM ubuntu:20.04

RUN apt-get update && apt-get install -y vsftpd && rm -rf /var/lib/apt/lists/*

COPY setup.sh /app/setup.sh
COPY vsftpd.conf /etc/vsftpd/vsftpd.conf

CMD ["bash", "/app/setup.sh"]
