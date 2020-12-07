import sys


def read_input(input_file):
    '''Read the input for day 5, part 1, and return it in digestible chunks'''
    try:
        with open(input_file, 'r') as inp:
            input_str = inp.read()
            input_ls = [x for x in input_str.split('\n') if x != '']
            return input_ls
    except:
        print(f'Failed to open input file {input_file} with error: {sys.exc_info()}')
        sys.exit(1)


def main():
    input_file = 'input.txt'
    boarding_passes = read_input(input_file)
    for bp in boarding_passes:
        print(bp)


if __name__ == '__main__':
    main()
