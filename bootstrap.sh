#!/bin/sh

export FLASK_APP=things
export FLASK_ENV=development
source $(pipenv --venv)/bin/activate

flask run
