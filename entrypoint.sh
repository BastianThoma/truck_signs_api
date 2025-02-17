#!/usr/bin/env bash
set -e

echo "Waiting for postgres to connect ..."

while ! nc -z trucksigns_db_container 5432; do
  sleep 1
done

echo "PostgreSQL is active"

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate

echo "Postgresql migrations finished"

python manage.py createsuperuser --noinput
echo "Creating superuser ..."

#gunicorn truck_signs_designs.wsgi:application --bind 0.0.0.0:8000
python manage.py runserver 0.0.0.0:8000