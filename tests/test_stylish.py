from gendiff import stylish
import pytest


@pytest.fixture(params=["1", "2"])
def result_string(request):
    file = open(f"tests/fixtures/stylish_result_{request.param}.txt")
    return file.read(), request.param


def test_stylish_converter(result_string, test_diff, mini_diff):
    result, fixt_id = result_string
    if fixt_id == 1:
        assert stylish(test_diff) == result
    if fixt_id == 2:
        assert stylish(mini_diff) == result
