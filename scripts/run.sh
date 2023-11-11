#!/bin/bash

source venv/bin/activate
gunicorn --access-logfile - --workers 3 --bind unix:/home/alpha-yaproq/yaproq.sock main.wsgi:application
