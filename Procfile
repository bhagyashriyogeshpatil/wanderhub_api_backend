release: python manage.py makemigrations && python manage.py migrate
web: gunicorn wanderhub_api_backend.wsgi