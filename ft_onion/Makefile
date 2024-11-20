all: up

up:
	docker-compose up -d

address:
	docker-compose exec tor cat /var/lib/tor/hidden_service/hostname

down:
	docker-compose down

logs:
	docker-compose logs -f

.PHONY: all up address down logs