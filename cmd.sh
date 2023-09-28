#!/bin/bash

./manage.py runserver 0.0.0.0:8000 &
python -m celery -A my_app worker -l info  