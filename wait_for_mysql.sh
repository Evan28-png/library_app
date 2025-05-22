#!/bin/sh
while ! nc -z db 3306; do
  echo "Waiting for MySQL to start..."
  sleep 1.4
done
echo "MySQL is up!"
exec flask db upgrade && gunicorn app:app --bind 0.0.0.0:3000

