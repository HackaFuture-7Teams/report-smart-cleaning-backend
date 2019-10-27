#!/usr/bin/env bash
export DEBIAN_FRONTEND=noninteractive &&
#pypy3 manage.py collectstatic --noinput -c &&
#pypy3 manage.py compilemessages &&
pypy3 manage.py migrate &&
#pypy3 manage.py runserver 0.0.0.0:8000
gunicorn core.wsgi -w 3 --bind=0.0.0.0 --timeout 120 --reload
