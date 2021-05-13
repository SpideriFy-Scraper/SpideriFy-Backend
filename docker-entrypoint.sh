#!/usr/bin/env bash

set -o errexit
set -o nounset

readonly cmd="$*"


# Evaluating Database Initiation Commnads
python3 manage.py db upgrade


# Evaluating passed command (do not touch):
# shellcheck disable=SC2086
exec $cmd
