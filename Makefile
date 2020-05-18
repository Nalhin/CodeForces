.PHONY: download test test_coverage format

get_problem:
	python templates/download_problem.py

test:
	coverage run -m unittest discover

test_coverage:
	coverage report -m

format:
	poetry run black solutions
