from gendiff import parser, creat_diff, stylish, plain, to_json


def generate_diff(fir_file, sec_file, format='stylish'):
    first_data = parser(fir_file)
    second_data = parser(sec_file)
    diff = creat_diff(first_data, second_data)
    match format:
        case 'stylish':
            return stylish(diff)
        case 'plain':
            return plain(diff)
        case 'json':
            return to_json(diff)
