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
	@which python3
	@echo "Done!"

.PHONY: all env clean