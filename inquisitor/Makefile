all: build up

build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

clean:
	docker-compose down -v
	docker system prune -f

logs:
	docker-compose logs -f

.PHONY: build up down clean logs