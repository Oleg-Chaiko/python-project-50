import pytest
from gendiff import generate_diff


@pytest.fixture()
def result_string():
    file = open('tests/fixtures/stylish_result_1.txt')
    return file.read()


def test_stylish_converter(result_string):
    file_1_path = 'tests/fixtures/file1.json'
    file_2_path = 'tests/fixtures/file2.json'
    format = 'stylish'
    assert generate_diff(file_1_path, file_2_path, format) == result_string
