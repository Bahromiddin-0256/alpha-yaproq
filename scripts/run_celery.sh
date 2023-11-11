#!/bin/bash

source venv/bin/activate
celery -A main worker -l info
