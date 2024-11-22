FROM ubuntu:20.04

RUN apt-get update && apt-get install -y vsftpd && rm -rf /var/lib/apt/lists/*

COPY vsftpd.conf /etc/vsftpd.conf

RUN useradd -m $FTP_USER && \
	echo "$FTP_USER:$FTP_PASS" | chpasswd && \
	chown -R $FTP_USER:$FTP_USER /home/$FTP_USER/ftp

EXPOSE 21 21000-21010

CMD ["/usr/sbin/vsftpd", "/etc/vsftpd.conf"]
