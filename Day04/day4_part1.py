import sys


def read_input(input_file):
    '''Read the input for the puzzle'''
    try:
        with open(input_file, 'r') as inp:
            input_str = inp.read()
            input_list = input_str.split('\n\n')
            return input_list
    except FileNotFoundError:
        print(f'Failed to read input file {input_file} because it was not found.')
        sys.exit(1)
    except PermissionError:
        print(f'Found input file {input_file}, but permissions do not allow reading it.')
        sys.exit(1)


def main():
    try:
        test = sys.argv[1]
        if test == 'test':
            input_file = 'test_input.txt'
        else:
            raise IndexError
    except IndexError:
        input_file = 'input.txt'

    passports = read_input(input_file)
    for passport in passports:
        print(passport + '\n')


if __name__ == '__main__':
    main()
