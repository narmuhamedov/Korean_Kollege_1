DC = docker compose
EXEC = docker exec -it
DB_CONTAINER = kkc_db
APP_CONTAINER = kkc_web
LOGS = docker logs -f


# для создания контейнеров
.PHONY: build
build:
	${DC} build

# для запуска контейнеров
.PHONY: up
up:
	${DC} up -d

# для перезапуска контейнеров
.PHONY: rerun
rerun:
	${DC} build && ${DC} up -d

# для остановки контейнеров
.PHONY: d
d:
	${DC} down

# для логов приложения
.PHONY: weblogs
weblogs:
	${LOGS} ${APP_CONTAINER}

# для логов БД
.PHONY: dblogs
dblogs:
	${LOGS} ${DB_CONTAINER} -f

# для выполнения команд в контейнере
.PHONY: bash
bash:
	${EXEC} ${APP_CONTAINER} bash

# для перехода в интерактивный питон в контейнере
.PHONY: py
py:
	${EXEC} ${APP_CONTAINER} python3