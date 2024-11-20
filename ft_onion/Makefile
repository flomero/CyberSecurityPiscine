all: up

up:
	docker-compose up -d

address:
	@docker-compose exec tor cat /var/lib/tor/hidden_service/hostname

down:
	docker-compose down

stop:
	docker-compose stop

clean:
	docker-compose down -v

fclean:
	docker system prune -a

logs:
	docker-compose logs -f

download-tor:
	curl -O https://dist.torproject.org/torbrowser/14.0.2/tor-browser-linux-x86_64-14.0.2.tar.xz
	tar -xf tor-browser-linux-x86_64-14.0.2.tar.xz
	rm tor-browser-linux-x86_64-14.0.2.tar.xz

run-tor:
	cd tor-browser && ./start-tor-browser.desktop

.PHONY: all up address down logs clean fclean download-tor

# ssh -p 4242 -o ProxyCommand='nc -x 127.0.0.1:9150 %h %p' 