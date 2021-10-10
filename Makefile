
all: setup

setup:
	@echo "\n-------------- Starting docker containers\n"
	@docker-compose -f ./api/docker-compose.yml up -d
	@echo "\n------------ Done!\n"
	@echo "... Starting front-end server"
	@yarn --cwd ./front start
	@echo "\n------------ Done!\n"


stop:
	@echo "\n-------------- Stopping docker containers\n"
	@docker-compose -f ./api/docker-compose.yml down
	@echo "\n------------ Done!\n"