#!/bin/bash

source venv/bin/activate
celery -A main beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler