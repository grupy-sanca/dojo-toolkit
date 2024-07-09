SHELL := bash
.PHONY: clean

.PHONY: install
install:
	poetry install

.PHONY: test
test:
	poetry run pytest -vv --cov=dojo_toolkit --cov-report=term-missing

.PHONY: lint
lint:
	@echo "Checking lock file"
	poetry check --lock
	@echo "Checking code"
	poetry run ruff check .

.PHONY: format
format:
	poetry run ruff format .

.PHONY: build
build: clean
	poetry build

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
