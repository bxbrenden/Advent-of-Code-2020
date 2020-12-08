import sys


def read_input(input_file):
    '''Get the input file into list form and return it'''
    try:
        with open(input_file, 'r') as inp:
            input_str = inp.read()
            input_list = [x for x in input_str.split('\n\n') if x != '']
            return input_list
    except:
        print(f'Failed to read input file: {sys.exc_info()}')
        sys.exit(1)


def main():
    input_file = 'input.txt'
    questions = read_input(input_file)

    for q in questions:
        print(q)


if __name__ == '__main__':
    main()
