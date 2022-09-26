FROM python:3.7-slim-buster AS build-stage

ENV LANG=C.UTF-8 \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  # pip:
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # poetry:
  POETRY_VERSION=1.1.10 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_HOME="/opt/poetry" \
  POETRY_CACHE_DIR='/var/cache/pypoetry'

RUN apt-get -y update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    rm -rf /var/lib/apt/lists/* && \
    pip install "poetry==$POETRY_VERSION" && poetry --version

WORKDIR /opt/kabum

# Install Python dependencies with Poetry
ADD pyproject.toml /opt/kabum/
RUN poetry install --no-dev --no-interaction --no-ansi

RUN groupadd -g 1001 app && useradd -u 1001 app -g app

# Cleaning poetry installation's cache for production
RUN rm -rf "$POETRY_CACHE_DIR"
COPY src/ ./src

RUN chown -R app:app .

USER app

CMD ["uvicorn", "src.main:app", "--host=0.0.0.0","--port=8000","--reload"]
