#!/usr/bin/env bash
set -e

# Activate virtualenv if present (Render sets up a venv automatically).
# Run Django's collectstatic (safeguard) and start gunicorn pointing to WSGI app.
echo "Collecting static files..."
python manage.py collectstatic --noinput || true

echo "Starting Gunicorn..."
exec gunicorn myproject.wsgi:application --bind 0.0.0.0:$PORT
