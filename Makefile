DC = docker compose
EXEC = docker exec -it
DB_CONTAINER = kkc_db
APP_CONTAINER = kkc_web
LOGS = docker logs -f


.PHONY: build
build:
	${DC} build

.PHONY: up
up:
	${DC} up -d

.PHONY: rerun
rerun:
	${DC} build && ${DC} up -d

.PHONY: d
d:
	${DC} down

.PHONY: weblogs
weblogs:
	${LOGS} ${APP_CONTAINER}

.PHONY: dblogs
dblogs:
	${LOGS} ${DB_CONTAINER} -f

.PHONY: bash
bash:
	${EXEC} ${APP_CONTAINER} bash

.PHONY: py
py:
	${EXEC} ${APP_CONTAINER} python3