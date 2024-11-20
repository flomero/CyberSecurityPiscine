from debian:bullseye

RUN apt update && apt upgrade -y && apt install -y \
	nginx \
	openssh-server \
	bash \
	nano

RUN ln -sf /bin/bash /bin/sh

RUN useradd -ms /bin/bash user && \
	echo 'user:user' | chpasswd

RUN chown -R user:user /var/www
RUN chmod 755 /var/www

CMD service ssh start && nginx -g 'daemon off;'


