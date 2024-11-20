from debian:bullseye

RUN apt update && apt upgrade -y && apt install -y \
	nginx \
	openssh-server

RUN useradd -ms /bin/bash user
RUN echo 'user:user' | chpasswd

CMD service ssh start && nginx -g 'daemon off;'


