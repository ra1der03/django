#!/bin/bash

cd /home/user/django/django_testing
git pull origin main
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
deactivate
sudo systemctl restart gunicorn
