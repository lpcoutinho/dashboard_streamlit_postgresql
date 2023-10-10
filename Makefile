.PHONY: install, format

PYTHON_SCRIPT = resources/createDB.py

createdb:
	python $(PYTHON_SCRIPT)
format:
	@isort .
	@black .



