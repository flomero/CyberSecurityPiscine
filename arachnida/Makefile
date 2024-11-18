ENV_DIR = env

all: env

env:
	@echo "Creating virtual environment..."
	@virtualenv $(ENV_DIR)
	@echo "Activating virtual environment..."
	@. $(ENV_DIR)/bin/activate
	@echo "Installing dependencies..."
	@pip install -r requirements.txt
	@echo "Done!"

clean:
	@echo "Cleaning up..."
	@rm -rf $(ENV_DIR)
	@echo "Done!"

.PHONY: all env clean