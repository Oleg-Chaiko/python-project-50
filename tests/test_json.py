from gendiff import to_json
import pytest
import json

@pytest.fixture()
def result_string():
    file = open(f"tests/fixtures/json_result.json")
    data = json.load(file)
    return json.dumps(data)



def test_json_converter(result_string, test_diff):
    assert to_json(test_diff) == result_string