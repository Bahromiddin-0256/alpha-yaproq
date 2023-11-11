#!/bin/bash

source venv/bin/activate
uvicorn main.asgi:application --uds /home/alpha-yaproq/yaproq.sock
