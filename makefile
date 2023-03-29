installrequirements:
	pip install -r requirements.txt
addrequirements:
	pip freeze > requirements.txt
starthttps:
	gunicorn --certfile=selfsigned.crt --keyfile=selfsigned.key -w 2 -b 77.79.185.10:2443 utv.wsgi
getssl:
	sudo openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout ./selfsigned.key -out ./selfsigned.crt
migrate:
	python manage.py makemigrations
	python manage.py migrate
dev:
	python manage.py runserver
lint:
	flake8
