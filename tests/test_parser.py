import pytest
from gendiff import parser


@pytest.fixture(params=["json", "yml"])
def parser_pararms(request):
    file_path = (f'tests/fixtures/file1.{request.param}')
    return file_path


def test_parser(parser_pararms, dict_1):
    assert parser(parser_pararms) == dict_1
