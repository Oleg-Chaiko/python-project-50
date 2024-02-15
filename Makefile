install:
	poetry install

test:
	poetry run pytest -vv

lint:
	poetry run flake8 gendiff

stylish: 
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.yaml

plain:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.yaml --format plain