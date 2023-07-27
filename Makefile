.PHONY: clean
clean: clean-eggs clean-build
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -delete

.PHONY: clean-eggs
clean-eggs:
	@find . -name '*.egg' -print0|xargs -0 rm -rf --
	@rm -rf .eggs/

.PHONY: clean-build
clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

.PHONY: ruff
ruff:
	poetry run ruff . --fix

.PHONY: ruffcheck
ruffcheck:
	@echo "Checking ruff..."
	poetry run ruff .

.PHONY: black
black:
	poetry run black .

.PHONY: blackcheck
blackcheck:
	@echo "Checking black..."
	poetry run black --check --diff .

.PHONY: build
build: clean
	poetry build

.PHONY: install
install:
	poetry install

.PHONY: poetrycheck
poetrycheck:
	poetry lock --check

.PHONY: pyformatcheck
pyformatcheck: poetrycheck blackcheck ruffcheck

.PHONY: lint
lint: pyformatcheck

.PHONY: format
format: ruff black

.PHONY: test
test: lint
	poetry run pytest

SHELL := bash
