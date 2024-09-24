release: python manage.py makemigrations && python manage.py migrate
web: gunicorn wanderhub-api-backend.wsgi