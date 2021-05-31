# docker build -t spiderify-api:prod --network host . -f Dockerfile
# docker run -d --name api-prod -v <Path-to>/common/sentiment_model/1:/app/common/sentiment_model/1 -p 8000:8080 spiderify-api:prod
# docker system df -v
# docker stats <container name>
# docker logs <container name>

# `python-base` sets up all our shared environment variables
FROM python:3.8-slim AS python-base

LABEL Maintainer "Homayoon Sadeghi <homayoon.9171@gmail.com>"
LABEL Vendor "SpideriFy"

    # python
ENV PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    # build:
    PRODUCTION_ONLY_PACKAGES='iputils-ping default-libmysqlclient-dev' \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # poetry
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    POETRY_VERSION=1.1.6 \
    # make poetry install to this location
    POETRY_HOME="/opt/poetry" \
    # make poetry create the virtual environment in the project's root
    # it gets named `.venv`
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1 \
    # paths
    # this is where our requirements + virtual environment will live
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv" \
    # tini:
    TINI_VERSION=v0.19.0 \
    TINI_PATH="/usr/local/bin/tini"


# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"


# `builder-base` stage is used to build deps + create our virtual environment
FROM python-base as builder-base
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install --no-install-recommends -y \
    bash \
    build-essential \
    curl \
    git \
    wget \
    libpq-dev \
    apt-transport-https \
    ca-certificates \
    software-properties-common \
    ${PRODUCTION_ONLY_PACKAGES}

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

# Installing `tini` utility:
# https://github.com/krallin/tini
RUN wget -O /usr/local/bin/tini "https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini" \
    && chmod +x /usr/local/bin/tini \
    && tini --version

# copy project requirement files here to ensure they will be cached.
WORKDIR ${PYSETUP_PATH}
COPY poetry.lock pyproject.toml ./

# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN poetry install --no-dev


# `development` image is used during development / testing
FROM python-base as development
ENV FLASK_ENV=development
WORKDIR ${PYSETUP_PATH}

# copy in our built poetry + venv
COPY --from=builder-base ${POETRY_HOME} ${POETRY_HOME}
COPY --from=builder-base ${PYSETUP_PATH} ${PYSETUP_PATH}

# quicker install as runtime deps are already installed
RUN poetry install

# will become mountpoint of our code
COPY . /app
WORKDIR /app
EXPOSE 8080

CMD [ "python3", "app.py" ]


# `production` image used for runtime
FROM python-base as production
ENV FLASK_ENV=production
WORKDIR ${PYSETUP_PATH}

# copy in our built poetry + venv
COPY --from=builder-base ${PYSETUP_PATH} ${PYSETUP_PATH}
COPY --from=builder-base ${TINI_PATH} ${TINI_PATH}
# install Some Packages
RUN apt -y update && apt install -y ${PRODUCTION_ONLY_PACKAGES} netcat
# will become mountpoint of our code
COPY . /app
WORKDIR /app
EXPOSE 8080

RUN chmod +x ./docker-entrypoint.sh
# We customize how our app is loaded with the custom entrypoint:
ENTRYPOINT ["tini", "--" , "./docker-entrypoint.sh"]
