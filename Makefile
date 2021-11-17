clean: clean-eggs clean-build
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -delete

clean-eggs:
	@find . -name '*.egg' -print0|xargs -0 rm -rf --
	@rm -rf .eggs/

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

build: clean
	poetry build

install:
	poetry install

format: install
	poetry run black .
	poetry run isort .

lint: install
	poetry run flake8 dojo_toolkit tests --max-line-length 100
	poetry run black . --check
	poetry run isort . --check-only --diff

test: lint
	poetry run pytest
