all: up

up:
	@docker-compose up -d

down:
	@docker-compose down

stop:
	@docker-compose stop

clean:
	@docker-compose down -v

fclean:
	@docker system prune -a

logs:
	@docker-compose logs -f

.PHONY: all up address down logs clean fclean