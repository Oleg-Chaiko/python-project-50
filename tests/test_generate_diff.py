from gendiff import generate_diff


def test_generate_diff(dict_1, dict_2, test_diff):
    assert generate_diff(dict_1, dict_2) == test_diff


def test_min_gen_diff(mini_dict_1, mini_dict_2, mini_diff):
    assert generate_diff(mini_dict_1, mini_dict_2) == mini_diff