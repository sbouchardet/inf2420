.PHONY: setup run test

setup:
	@pip install -r requirements.txt

run:
	@jupyter notebook

test:
	@nosetests -s