DEV_IMAGE=app-streamlit-dev:latest
PROD_IMAGE=app-streamlit-prod:latest

# Default target: display help
help:
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "    make %-15s - %s\n", $$1, $$2}'
.PHONY: help

# docker builds
build-dev:  ## build docker DEV image
	DOCKER_BUILDKIT=1 docker build -t $(DEV_IMAGE) --target=dev . 
.PHONY: build-dev

build-prod:  ## build docker PROD image
	DOCKER_BUILDKIT=1 docker build -t $(PROD_IMAGE) --target=prod . 
.PHONY: build-prod

# lint - local
lint:  ## run ruff lint checks locally, requires instalation of dependencies
	ruff check . --config pyproject.toml
.PHONY: lint

lint-fix:  ## fixes issues found by ruff linting
	ruff check . --config pyproject.toml --fix
.PHONY: lint-fix

# lint - docker
docker-lint:  ## run ruff lint checks in DEV docker container
	@if docker images --format '{{.Repository}}:{{.Tag}}' | grep -q "^$(DEV_IMAGE)$$"; then \
		docker run -it --rm $(DEV_IMAGE) ruff check .; \
	else \
		echo "Image $(DEV_IMAGE) does not exist.\nRun:\n> \033[0;31m make build-dev \033[0m "; \
		exit 1; \
	fi
.PHONY: docker-lint
