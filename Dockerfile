FROM 3.8-slim-buster

LABEL Maintainer "Homayoon Sadeghi <homayoon.9171@gmail.com>"
LABEL Vendor "Poetry.services"

ARG FLASK_ENV

ENV FLASK_ENV=${FLASK_ENV} \
    # build:
    BUILD_ONLY_PACKAGES='wget' \
    # python:
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    # pip:
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    # tini:
    TINI_VERSION=v0.19.0 \
    # poetry
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_VERSION=1.1.6

# System deps:
RUN apt-get update && apt-get upgrade -y \
  && apt-get install --no-install-recommends -y \
    bash \
    build-essential \
    curl \
    git \
    libpq-dev \
    # Defining build-time-only dependencies:
    $BUILD_ONLY_PACKAGES \
    # Installing `tini` utility:
    # https://github.com/krallin/tini
    && wget -O /usr/local/bin/tini "https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini" \
    && chmod +x /usr/local/bin/tini && tini --version \
    # Removing build-time-only dependencies:
    && apt-get remove -y $BUILD_ONLY_PACKAGES \
    # Cleaning cache:
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Installing `poetry` package manager:
# https://github.com/python-poetry/poetry
RUN pip3 install --upgrade pip && \
    pip3 install "poetry==$POETRY_VERSION"


WORKDIR /app

# Copy only requirements, to cache them in docker layer
COPY poetry.lock pyproject.toml /app/
ENV PYTHONPATH=${PYTHONPATH}:${PWD}


# Project initialization:
RUN poetry config virtualenvs.create false
RUN echo "$FLASK_ENV" \
  && poetry install \
    $(if [ "$FLASK_ENV" = 'production' ]; then echo '--no-dev'; fi) \
    --no-interaction --no-ansi \
  # Cleaning poetry installation's cache for production:
  && if [ "$FLASK_ENV" = 'production' ]; then rm -rf "$POETRY_CACHE_DIR"; fi
RUN pip3 uninstall --yes poetry
COPY . /app

EXPOSE 8080

# We customize how our app is loaded with the custom entrypoint:
ENTRYPOINT ["/tini", "--"]
# Run your program under Tini
CMD [ "python3", "app.py" ]
