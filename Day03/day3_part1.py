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


def find_min_grid_width(rows):
    '''Given an int `rows`, find the minimum width (chars) a grid can be to allow right-3, down-1 traversal'''
    if rows > 1:
        return rows * 3 + -2
    else:
        return 4


def construct_repeated_grid(grid, min_width):
    '''Given a list of strings representing grid rows, return a list of strings where each row is repeated
       enough times to support a minimum width of `min_width`.'''
    ...


def main():
    input_file = 'test_input.txt'
    grid = read_input(input_file)
    for l in grid:
        print(l)

    rows = len(grid)
    min_width = find_min_grid_width(rows)
    print(f'The minimum grid width is: {min_width}')


if __name__ == '__main__':
    main()
