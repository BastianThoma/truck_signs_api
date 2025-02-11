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

if [ -f truck_signs_designs/settings/.env ]; then
  export $(grep -v '^#' truck_signs_designs/settings/.env | xargs)
fi;

if [ -z "$DJANGO_SUPERUSER_USERNAME" ] || [ -z "$DJANGO_SUPERUSER_EMAIL" ] || [ -z "$DJANGO_SUPERUSER_PASSWORD" ]; then
  echo "Superuser data is not set. Please check the .env file."
  exit 1
fi;

echo "Creating superuser ..."

PYTHONPATH=/app python /app/truck_signs_designs/scripts/create_superuser.py

gunicorn truck_signs_designs.wsgi:application --bind 0.0.0.0:8000