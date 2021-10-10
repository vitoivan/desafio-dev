REGISTER = register_cnab.py

all: setup test

setup:
	@echo "\n... Starting the virtual environment\n"
	@./setup_venv.sh
	@echo "\n... Done!\n"

test:
	@echo "\n... Starting tests\n"
	@python $(REGISTER)
	@echo "\n... Done!\n"