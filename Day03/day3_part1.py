from collections import Counter
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
    #print(f'The current width of the grid is {current_width}')
    #print(f'In order to support right-3, down-1 traversal, the grid needs to be {min_width} characters wide')
    repeats = math.ceil(min_width / current_width)
    #print(f'We need to repeat the grid from left to right {repeats} times')

    return [row * repeats for row in grid]


def test_grid_construction(test_grid, rep_grid):
    '''Given the name of a file `test_grid`, read it and compare it to a repeated grid constructed by
       the `construct_repeated_grid` function.
       Return True if the grids are the same, otherwise False

       The purpose of this test is to make sure that my repeated grid looks like the one from the example'''

    test_grid = read_input(test_grid)
    return test_grid == rep_grid


def right_3_down_1(grid, row_num, index):
    '''Using the grid `grid`, traverse it right 3, down 1, landing on a character in each subsequent row.
       Start traversing from row number `row_num` at index `index`.
       Place an 'X' on the landing spot (row + 1, index + 3) if there was originally a '#'(tree) there.
       Otherwise, place an 'O' there if there was originally a '.' (opening) there'''

    try:
        next_row = grid[row_num + 1]
    except IndexError:
        return

    landing_index = index + 3
    #print(f'the landing index is {landing_index}')
    try:
        landing_spot = next_row[landing_index]
    except IndexError:
        return

    #print(f'the landing spot character is {landing_spot}')
    if landing_spot == '.':
        next_row = list(next_row)
        next_row[landing_index] = 'O'
        next_row = ''.join(next_row)
        return next_row
    elif landing_spot == '#':
        next_row = list(next_row)
        next_row[landing_index] = 'X'
        next_row = ''.join(next_row)
        return next_row


def create_filled_grid(grid):
    '''Starting with an unfilled grid, begin on row 0, index 0, and fill it out by traversing 3 over, 1 down'''

    # Initialize the new, filled grid with the first row of the old grid since they're the same
    filled = [grid[0]]
    for row_num, _ in enumerate(grid):
        index = row_num * 3
        next_row = right_3_down_1(grid, row_num, index)
        if next_row:
            filled.append(next_row)

    return filled


def count_trees(filled_grid):
    '''Once a grid is filled in, we can use this function to count the number of "trees" (X characters)'''
    flattened_grid = [item for sublist in filled_grid for item in sublist]
    char_count = Counter(flattened_grid)
    num_trees = char_count['X']

    return num_trees


def main():
    input_file = 'test_input.txt'
    grid = read_input(input_file)

    rows = len(grid)
    min_width = find_min_grid_width(rows)

    rep_grid = construct_repeated_grid(grid, min_width)
    filled_grid = create_filled_grid(rep_grid)

    for row in filled_grid:
        print(row)

    num_trees = count_trees(filled_grid)
    print(f'ANSWER: the number of trees is {num_trees}')


if __name__ == '__main__':
    main()
