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
	@chmod +x spider.py
	@chmod +x scorpion.py
	@$(ACTIVATE) && which python3
	@echo "Done!"

clean:
	@echo "Cleaning up..."
	@rm -rf $(ENV_DIR)
	@echo "Done!"

.PHONY: all env clean