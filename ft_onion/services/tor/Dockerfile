from debian:bullseye

RUN apt update && apt upgrade -y && apt install -y \
	tor

EXPOSE 9050

USER tor

CMD ["tor", "-f", "/etc/tor/torrc"]