#!/usr/bin/env bash

set -o errexit
set -o nounset

readonly cmd="$*"


# Evaluating Database Initiation Commnads
exec python manage.py db init
exec python manage.py db migrate
exec python manage.py db upgrade


# Evaluating passed command (do not touch):
# shellcheck disable=SC2086
exec $cmd
