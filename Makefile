runserver:
	python manage.py runserver

newapp:
	python manage.py startapp userapp

runtest:
	python manage.py test user_app.test.test_models

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate