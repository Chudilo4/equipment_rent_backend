installrequirements:
	pip install -r requirements.txt
addrequirements:
	pip freeze > requirements.txt
start:
	gunicorn --bind 0.0.0.0:8000 equipment.wsgi
migrate:
	python manage.py makemigrations
	python manage.py migrate
dev:
	python manage.py runserver
lint:
	flake8
