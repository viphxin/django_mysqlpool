all: usage
usage:
		@echo usage:
		@echo make clean, delete the auto-generated files and directories.
		@echo make build, build the project

build:
		python setup.py bdist_egg

clear:
		rm -rf dist build ./codoon_mysqlpool.egg-info

distribute:
		python setup.py sdist
