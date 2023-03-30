FROM python:3.11-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Additional dependencies
  && apt-get install -y telnet netcat \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Set on deployment to redeploy requirements
ARG CACHE_BUST=1

# Requirements are installed here to ensure they will be cached.
COPY ./python-requirements/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /app

ENTRYPOINT ["/app/scripts/wait_for_db.sh"]