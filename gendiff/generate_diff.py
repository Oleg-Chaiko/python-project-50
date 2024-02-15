from gendiff import parser, creat_diff, stylish, plain, to_json


def get_result(first_file, second_file, format):
    diff = generate_diff(first_file, second_file)
    match format:
        case 'stylish':
            return stylish(diff)
        case 'plain':
            return plain(diff)
        case 'json':
            return to_json(diff)


def generate_diff(fir_file, sec_file):
    first_data = parser(fir_file)
    second_data = parser(sec_file)
    diff = creat_diff(first_data, second_data)
    return diff
