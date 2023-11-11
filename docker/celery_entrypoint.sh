#!/bin/bash
echo "--> Starting celery process"
celery -A core beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
