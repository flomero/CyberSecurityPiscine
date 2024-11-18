ENV_DIR = env
SHELL := /bin/bash

all: env

env:
	@echo "Creating virtual environment..."
	@virtualenv $(ENV_DIR)
	@echo "Activating virtual environment..."
	@. $(ENV_DIR)/bin/activate
	@echo "Installing dependencies..."
	@pip install -r requirements.txt
	@chmod +x spider.py
	@chmod +x scorpion.py
	@echo "Done!"

.PHONY: all env clean