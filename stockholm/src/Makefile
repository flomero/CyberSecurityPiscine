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
	@curl -L https://gist.githubusercontent.com/MattIPv4/045239bc27b16b2bcf7a3a9a4648c08a/raw/2411e31293a35f3e565f61e7490a806d4720ea7e/bee%2520movie%2520script > ./infection/bee_movie.txt
	@curl -L https://upload.wikimedia.org/wikipedia/en/e/ed/Nyan_cat_250px_frame.PNG > ./infection/nyan_cat.png

remove-dummy-files:
	@rm -rf ./infection

.PHONY: all up address down logs clean fclean create-dummy-files remove-dummy-files