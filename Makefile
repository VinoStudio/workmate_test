CONTAINER_NAME = workmate_parser_container
IMAGE_NAME = workmate_parser_image
DOCKER_FILE = Dockerfile
VOLUME_PATH = $(shell pwd):/workmate_parser_test
SCRIPT = python main.py --file log_examples/example1.log log_examples/example2.log --report average

.PHONY: build run test test-verbose clean all

build:
	@echo "Building Docker image..."
	docker build -t $(IMAGE_NAME) -f $(DOCKER_FILE) .

test: build
	@echo "Running tests..."
	docker run --rm --name $(CONTAINER_NAME) $(IMAGE_NAME) pytest

shell: build
	@echo "Running a shell in the container..."
	docker run --rm --name $(CONTAINER_NAME) -v $(VOLUME_PATH) -it $(IMAGE_NAME) /bin/bash

run_script: build
	@echo "Running the script..."
	docker run --rm --name $(CONTAINER_NAME) -v $(VOLUME_PATH) $(IMAGE_NAME) $(SCRIPT)

clean:
	@echo "Cleaning up..."
	docker rmi $(IMAGE_NAME)
	docker rm $(CONTAINER_NAME)

all: run_script test clean