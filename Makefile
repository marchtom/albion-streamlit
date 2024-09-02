lint:
	ruff check . --config pyproject.toml
.PHONY: lint

lint-fix:
	ruff check . --config pyproject.toml --fix
.PHONY: lint-fix

# lint - docker
docker-lint:
	@if docker images --format '{{.Repository}}:{{.Tag}}' | grep -q "^$(DEV_IMAGE)$$"; then \
		docker run -it --rm $(DEV_IMAGE) ruff check .; \
	else \
		echo "Image $(DEV_IMAGE) does not exist.\nRun:\n> \033[0;31m make build-dev \033[0m "; \
		exit 1; \
	fi
.PHONY: docker-lint
