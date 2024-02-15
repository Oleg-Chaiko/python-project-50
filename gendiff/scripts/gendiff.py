import argparse
from gendiff import generate_diff


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
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == 'main':
    main()
