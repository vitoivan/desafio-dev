all: disable-postgres start

start: setup-back setup-front start-servers

stop: stop-docker active-postgres

start-servers: start-docker start-front


start-docker:
	@echo "\n-------------- Starting docker containers\n"
	@docker-compose -f ./api/docker-compose.yml up -d
	@echo "\n------------ Done!\n"

stop-docker:
	@echo "\n-------------- Stopping docker containers\n"
	@docker-compose -f ./api/docker-compose.yml down
	@echo "\n------------ Done!\n"


start-front:
	@echo "\n-------------- Starting front-end server"
	@yarn --cwd ./front start
	@echo "\n------------ Done!\n"

setup-front:
	@echo "\n-------------- Installing front dependencies\n"
	@yarn --silent --cwd ./front
	@echo "\n------------ Done!\n"


setup-back:
	@echo "\n-------------- Installing api dependencies\n"
	@./setup_venv.sh
	@echo "\n------------ Done!\n"

active-postgres:
	@echo "\n-------------- Starting your postgres process on port 5432 \n"
	@/etc/init.d/postgresql start
	@echo "\n------------ Done!\n"


disable-postgres:
	@echo "\n-------------- Stopping your process on port 5432 \n"
	@/etc/init.d/postgresql stop
	@echo "\n------------ Done!\n"


.PHONY: start-docker stop-docker start-front setup-front setup-back active-postgres disable-postgres
