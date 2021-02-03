#!/bin/bash

echo "Sleeping to allow database to initialize"
sleep 3.5
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('${django_admin}', '${django_email}', '${django_password}')" | python manage.py shell
python3 manage.py migrate
python3 manage.py runserver 0:${django_port}
