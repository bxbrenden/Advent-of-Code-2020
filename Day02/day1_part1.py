import sys
import re

def read_input(input_file):
    '''Read the input file and parse into usable chunks'''
    try:
        with open(input_file, 'r') as inp:
            input_str = inp.read()
            input_lines = [line for line in input_str.split('\n') if line != '']
            return input_lines
    except PermissionError:
        print(f'Input file {input_file} found, but permissions do not allow opening.')
        sys.exit(1)
    except FileNotFoundError:
        print(f'Input file {input_file} not found. Please make sure it exists.')
        sys.exit(1)


def main():
    input_file = 'input.txt'
    passwords = read_input(input_file)
    for p in passwords:
        print(p)


if __name__ == '__main__':
    main()
