import sys


def read_input(input_file):
    '''Given an input file, read it and return it in usable chunks'''
    try:
        with open(input_file, 'r') as inp:
            input_str = inp.read()
            input_list = [x for x in input_str.split('\n') if x != '']
            return input_list
    except PermissionError:
        print(f'File {input_file} was found, but permission does not allow it to be read.')
        sys.exit(1)
    except FileNotFoundError:
        print(f'File {input_file} was not found! Please make sure it exists.')
        sys.exit(1)


def main():
    input_file = 'test_input.txt'
    input_list = read_input(input_file)
    for l in input_list:
        print(l)


if __name__ == '__main__':
    main()
