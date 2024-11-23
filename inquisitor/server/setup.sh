#!/bin/bash

useradd -m $FTP_USER
echo "$FTP_USER:$FTP_PASS" | chpasswd
chown $FTP_USER:$FTP_USER /home/$FTP_USER

/usr/sbin/vsftpd /etc/vsftpd/vsftpd.conf