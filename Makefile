run:
	python manage.py runserver

newapp:
	python manage.py startapp userapp

runtest:
	python manage.py test user_app.test.test_models

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

createsuperuser:
	python manage.py createsuperuser

fill_db:
	python manage.py fill_db