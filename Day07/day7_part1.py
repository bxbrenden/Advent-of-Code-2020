import sys


def read_input(input_file):
    '''Read the input file and return it in digestible chunks'''
    try:
        with open(input_file, 'r') as inp:
            input_str = inp.read()
            input_list = input_str.split('\n')
            return input_list
    except:
        print(f'Failed to read specified input file {input_file} with exception {sys.exc_info()}')
        sys.exit(1)


def main():
    input_file = 'test_input.txt'
    bag_rules = read_input(input_file)

    for rule in bag_rules:
        print(rule)


if __name__ == '__main__':
    main()
