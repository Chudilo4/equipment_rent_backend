installrequirements:
	pip install -r requirements.txt
addrequirements:
	pip freeze > requirements.txt
start:
	gunicorn --bind 0.0.0.0:8000 equipment.wsgi
getssl:
	sudo openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout ./selfsigned.key -out ./selfsigned.crt
migrate:
	python manage.py makemigrations
	python manage.py migrate
dev:
	python manage.py runserver
lint:
	flake8
