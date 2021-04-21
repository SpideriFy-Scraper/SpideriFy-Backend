FROM python:3.8
LABEL maintainer "Homayoon Sadeghi <homayoon.9171@gmail.com>"
RUN mkdir /app
COPY ./poetry.lock ./pyproject.toml /app/
WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false && \
poetry install --no-interaction --no-ansi
COPY . /app/
EXPOSE 8080
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
