#!/bin/bash

source venv/bin/activate
gunicorn --access-logfile - --workers 3 --bind unix:/home/ponipora/ponipora.sock core.wsgi:application
