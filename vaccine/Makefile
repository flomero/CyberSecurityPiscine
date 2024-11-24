ENV_DIR = env
SHELL := /bin/bash

ACTIVATE = source $(ENV_DIR)/bin/activate

all: env

env:
	@echo "Creating virtual environment..."
	@virtualenv $(ENV_DIR)
	@echo "Activating virtual environment..."
	@echo "Installing dependencies..."
	@$(ACTIVATE) && pip install -r requirements.txt
	@echo "Done!"
	@echo "To activate the virtual environment, run: . $(ENV_DIR)/bin/activate"

clean:
	@echo "Cleaning up..."
	@rm -rf $(ENV_DIR)
	@echo "Done!"

run-dbs:
	docker compose -f mysql/docker-compose.yml up -d
	docker compose -f sqlite/docker-compose.yml up -d

myslq-logs:
	docker compose -f mysql/docker-compose.yml logs

sqlite-logs:
	docker compose -f sqlite/docker-compose.yml logs

db-logs: mysql-logs sqlite-logs

stop-dbs:
	docker compose -f mysql/docker-compose.yml down
	docker compose -f sqlite/docker-compose.yml down

.PHONY: all env clean run-dbs mysql-logs sqlite-logs stop-dbs