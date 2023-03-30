PYTHONPATH=$(shell pwd)/src

.EXPORT_ALL_VARIABLES:

# Python Commands

test:
	pytest -v test/unit/test_*.py

run:
	flask --app ./src/app.py --debug run --host=0.0.0.0

CELERY_OPTIONS ?=
celery-worker-start:
	celery -A app.celery worker --loglevel=info $(CELERY_OPTIONS)


# Docker commands

run-docker:
	docker-compose up -d

# Local commands

db-start:
	docker run -d -it --rm --name postgres -p 5432:5432 postgres

redis-start:
	docker run -d -it --rm --name redis -p 6379:6379 redis

run-local:
	make redis-start
	make run
	make celery-worker-start
