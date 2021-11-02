install:
	@ pip install -r requirements.txt

run_tests:
	@ pytest

run_tests_coverage:
	@ pytest --cov=problems --cov-report term-missing --cov-report xml:coverage/cov.xml --cov-report html:coverage/html
