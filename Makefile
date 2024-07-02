run:
	@$(MAKE) migrate
	@$(MAKE) fill_db
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
	python manage.py create_admin

fill_db:
	@$(MAKE) createsuperuser
	python manage.py fill_db
	python manage.py fill_courses
	@echo "База данных наполнена"


del_all:
	@docker stop $$(docker ps -aq) || true
	@docker rm $$(docker ps -aq) || true
	@echo "Контейнеры в Docker остановлены и удалены"

up_pg:
	@docker compose up -d pg
