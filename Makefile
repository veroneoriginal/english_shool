run:
	@$(MAKE) up_pg
	@$(MAKE) wait_for_db
	@$(MAKE) migrate
	@$(MAKE) fill_db
	python manage.py runserver

newapp:
	python manage.py startapp user_app

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

# Цель для ожидания готовности PostgreSQL
wait_for_db:
	@echo "Ожидание запуска PostgreSQL..."
	@until docker exec -it language_school pg_isready -U postgres; do \
	sleep 1; \
	done
	@echo "PostgreSQL готова к использованию."

coverage:
	coverage run --source='.' manage.py test
	coverage report --omit=settings/asgi.py,settings/wsgi.py,manage.py,mainapp/management/* --fail-under=80
	coverage html -d coverage_html_report --omit=settings/asgi.py,settings/wsgi.py,manage.py,mainapp/management/*

lint:
	pylint $(shell git ls-files '*.py')

go:
	docker start language_school

worker_go:
	python manage.py rqworker

up_redis:
	@docker compose up -d redis

# посмотреть статистику задач в очереди
look_statistics:
	python manage.py rqstats --interval=1

test_user_app:
	python manage.py test user_app

test_course_view:
	python manage.py test api.course.tests.test_courses_views

test_teachers_view:
	python manage.py test api.users.tests.test_teachers_views

test_registration_view:
	python manage.py test api.authentication.tests.test_registration_view

test_login_view:
	python manage.py test api.authentication.tests.test_login_view

test_all:
	python manage.py test user_app
	python manage.py test api.course.tests.test_courses_views
	python manage.py test api.users.tests.test_teachers_views
	python manage.py test api.authentication.tests.test_registration_view
	python manage.py test api.authentication.tests.test_login_view

start:
	python manage.py runserver
