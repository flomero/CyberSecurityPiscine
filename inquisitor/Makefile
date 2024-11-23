all: build up

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

clean:
	docker-compose down -v
	docker system prune -f

logs:
	docker-compose logs -f

arp:
	@echo client
	@docker exec -it ftp_client arp -a
	@echo "---------------------------------"
	@echo server
	@docker exec -it ftp_server arp -a

.PHONY: build up down clean logs