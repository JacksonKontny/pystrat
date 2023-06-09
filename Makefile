PYTHONPATH=$(shell pwd)/src

.EXPORT_ALL_VARIABLES:

# Testing

pytest:
	pytest -v

# docker-compose

run-docker:
	docker-compose up -d

stop-docker:
	docker-compose down

# Docker commands (used by docker-compose)

run:
	flask --app ./src/app.py --debug run --host=0.0.0.0

CELERY_OPTIONS ?=
celery-worker-start:
	celery -A app.celery worker --loglevel=info $(CELERY_OPTIONS)

# Local environment

db-start:
	docker run -d -it --rm --name postgres -p 5432:5432 postgres

redis-start:
	docker run -d -it --rm --name redis -p 6379:6379 redis

setup-python:
	python3 -m venv .venv
	(source .venv/bin/activate)
	pip install -r ./python-requirements/requirements-test.txt

run-local:
	make redis-start
	make run
	CELERY_OPTIONS=--detach make celery-worker-start