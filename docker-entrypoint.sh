#!/usr/bin/env bash
set -o errexit
set -o nounset

if [ "$DATABASE" = "mysql" ]
then
    echo "Waiting For MySQL..."
    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done
    echo "MySQL started"
fi

if [ "$FLASK_ENV" = "development" ]
then
    echo "Creating the database tables..."
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    echo "Tables created"
fi

if [ "$FLASK_ENV" = "production" ]
then
    echo "Creating the database tables..."
    python manage.py db upgrade
    echo "Tables created"
fi

exec "$@"
