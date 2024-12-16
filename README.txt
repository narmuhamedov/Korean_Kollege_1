# Документация по работе с проектом

Пока проект работает в режиме development, без докера, с докером работает в режиме production.

Для режима production есть:
- Свой requirements.prod.txt
- Dockerfile и docker-compose.yml, Makefile для простого запуска
- Свой файл настроек в settings/production.py
- Используется Postgres, для авторизации есть .env файл, который не загружается на github. следует создать свой по примеру .env-example

Для запуска в режиме production нужно выполнить команду `make build & make up`  или `make rerun`
Nginx в докер не входит

Для запуска в режиме разработки нужно выполнить команду `python manage.py runserver`
