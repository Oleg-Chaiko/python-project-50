from gendiff import plain
import pytest

@pytest.fixture(params=["1", "2"])
def result_string(request):
    file = open(f"tests/fixtures/plain_result_{request.param}.txt")
    return file.read(), request.param


def test_plain_converter(result_string, test_diff, mini_diff):
    result, fixt_id = result_string
    if fixt_id == 1:
        assert plain(test_diff) == result
    if fixt_id == 2:
        assert plain(mini_diff) == result