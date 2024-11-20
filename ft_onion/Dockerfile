from alpine:latest

RUN apk add --no-cache \
	tor \
	openssh-server

RUN ssh-keygen -A

EXPOSE 9050

RUN echo "root:root" | chpasswd

CMD ["tor", "-f", "/etc/tor/torrc"]