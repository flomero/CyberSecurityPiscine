from debian:bullseye

RUN apt update && apt upgrade -y && apt install -y \
	tor

RUN useradd -ms /bin/bash toruser
RUN chown -R toruser:toruser /etc/tor /var/lib/tor /var/log/tor

USER toruser
CMD service tor start