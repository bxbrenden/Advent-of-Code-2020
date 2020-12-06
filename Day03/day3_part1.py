import math
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
    current_width = len(grid[0])
    print(f'The current width of the grid is {current_width}')
    print(f'In order to support right-3, down-1 traversal, the grid needs to be {min_width} characters wide')
    repeats = math.ceil(min_width / current_width)
    print(f'We need to repeat the grid from left to right {repeats} times')

    return [row * repeats for row in grid]


def test_grid_construction(test_grid, rep_grid):
    '''Given the name of a file `test_grid`, read it and compare it to a repeated grid constructed by
       the `construct_repeated_grid` function.
       Return True if the grids are the same, otherwise False

       The purpose of this test is to make sure that my repeated grid looks like the one from the example'''

    test_grid = read_input(test_grid)
    return test_grid == rep_grid


def main():
    input_file = 'test_input.txt'
    grid = read_input(input_file)
    for l in grid:
        print(l)

    rows = len(grid)
    min_width = find_min_grid_width(rows)
    print(min_width)

    rep_grid = construct_repeated_grid(grid, min_width)


if __name__ == '__main__':
    main()
