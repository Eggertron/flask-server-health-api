#!/bin/bash

export FLASK_APP=health-api.py
flask run --host=0.0.0.0 --port=80
