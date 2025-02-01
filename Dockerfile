FROM python:3.11.3-slim-bullseye as base

ARG BUILD_ENVIRONMENT=local
ARG APP_HOME=/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

# Install required system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  # psycopg2 dependencies
  libpq-dev \
  # Translations dependencies
  gettext \
  gcc \
  python3-dev \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir files \
  && apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y --no-install-recommends curl gcc libpq-dev gettext python3-dev \
  && curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python - \
  && ln -s /opt/poetry/bin/poetry /usr/local/bin/poetry \
  && poetry config virtualenvs.create false \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-interaction --no-ansi --only main --no-root

# copy application code to WORKDIR
COPY . ${APP_HOME}
EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]