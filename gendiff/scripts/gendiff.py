import argparse
from gendiff import parser, generate_diff, stylish, plain, to_json


def get_result(first_file, second_file, format):
    first_data = parser(first_file)
    second_data = parser(second_file)
    diff = generate_diff(first_data, second_data)
    match format:
        case 'stylish':
            return stylish(diff)
        case 'plain':
            return plain(diff)
        case 'json':
            return to_json(diff)


def getargs():
    parser = argparse.ArgumentParser()
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", "--format",
                        help="output format, default='stylish'",
                        default='stylish')
    args = parser.parse_args()
    return args


def main():
    args = getargs()
    print(get_result(args.first_file, args.second_file, args.format))


if __name__ == 'main':
    main()
