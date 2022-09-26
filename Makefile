.ONESHELL:
ENV_PREFIX=$(shell python -c "if __import__('pathlib').Path('.venv/bin/pip').exists(): print('.venv/bin/')")
USING_POETRY=$(shell grep "tool.poetry" pyproject.toml && echo "yes")

.DEFAULT_GOAL := default_target

PROJECT_NAME := case-backend-kabum
PYTHON_VERSION := 3.7.12
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)
COVERAGE := 75

.PHONY: install
install:
	@if ! poetry --version > /dev/null; then echo 'poetry is required, install from https://python-poetry.org/'; exit 1; fi
	@rm -rf .venv
	@poetry install --no-interaction
	@echo "Please run 'poetry shell' or 'poetry run my_test_template'"

.PHONY: docker-build
docker-build:
	@docker build -t kabum-shipping:latest .

.PHONY: docker-run
docker-run:
	@docker run --name kabum-shipping-api -p 8000:8000 -d kabum-shipping

.PHONY: docker-stop
docker-stop:
	@docker stop kabum-shipping-api

.PHONY: docker-start
docker-start:
	@docker start kabum-shipping-api

.PHONY: docker-show-containers
docker-show-containers:
	@docker ps -la

.PHONY: docker-log
docker-logs:
	@docker logs -f kabum-shipping-api

.PHONY: docker-stuffs
docker-stuffs:
	@docker build -t kabum-shipping:latest .
	@docker run --name kabum-shipping-api -p 8000:8000 -d kabum-shipping
	@docker logs -f kabum-shipping-api

.PHONY: watch
watch:            ## Run tests on every change.
	ls **/**.py | entr $(ENV_PREFIX)pytest --picked=first -s -vvv -l --tb=long --maxfail=1 tests/

.PHONY: fmt
fmt:
	rm -rf test-results
	mkdir -p test-results
	isort src

.PHONY: lint
lint: fmt
	echo "Running pycodestyle"
	pycodestyle src || true
	python -m flake8 src --output-file=test-results/flake8.txt || true

.PHONY: test
test: lint        ## Run tests and generate coverage report.
	pytest -vv --cov=src --cov-report=term-missing --cov-report=html --cov-fail-under=$(COVERAGE)

.PHONY: clean
clean:            ## Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*.egg-info' -exec rm -rf {} +
	@find . -name '*.egg' -exec rm -f {} +
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf .eggs/
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build
	@rm -rf .coverage
	@rm -rf reports/
	@rm -rf coverage.xml
