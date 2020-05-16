.PHONY: download test test_coverage

get_problem:
	python templates/download_problem.py

test:
	coverage run -m unittest discover

test_coverage:
	coverage report -m