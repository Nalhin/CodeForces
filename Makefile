.PHONY: download test test_coverage format

get_problem:
	python templates/download_problem.py

test:
	poetry run coverage run -m unittest discover

test_coverage:
	poetry run coverage report -m

format:
	poetry run black solutions

lint:|
	poetry run flake8
	poetry run black solutions --check
