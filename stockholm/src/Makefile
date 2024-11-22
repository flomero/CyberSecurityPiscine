all: up

up:
	@docker-compose up -d

down:
	@docker-compose down

re: down up

stop:
	@docker-compose stop

clean:
	@docker-compose down -v

fclean:
	@docker system prune -a

logs:
	@docker-compose logs -f

create-dummy-files:
	@mkdir -p ./infection
	@echo "Hello\nI'm a file." > ./infection/hello.msg
	@echo "aaaaaaaaaahhhh help me" > ./infection/flag.txt
	@echo "i wanna cry" > ./infection/test.txt
	@echo "i'm fineeeee" > ./infection/hihi.exe
	@mkdir -p ./infection/inner
	@echo "Hello\nI'm a file." > ./infection/inner/another.txt
	@echo "echo hallo" > ./infection/inner/script.sh
	@mkdir -p ./infection/c
	@echo "int main() { return 0; }" > ./infection/c/helloworld.c

remove-dummy-files:
	@rm -rf ./infection

.PHONY: all up address down logs clean fclean create-dummy-files remove-dummy-files