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


def find_min_grid_width(rows, slope_x, slope_y):
    '''Given an int `rows` and a slope's x and y components, find the minimum width (chars) a
       grid can be to allow right-x, down-y traversal'''
    if rows > 1:
        return rows * slope_x - 2
    else:
        return slope_x + 1


def construct_repeated_grid(grid, min_width, X, Y):
    '''Given a list of strings representing grid rows, return a list of strings where each row is repeated
       enough times to support a minimum width of `min_width`.'''
    current_width = len(grid[0])
    print(f'The current width of the grid is {current_width}')
    print(f'In order to support right-{X}, down-{Y} traversal, the grid needs to be {min_width} characters wide')
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


def right_x_down_y(grid, row_num, index, slope_x, slope_y):
    '''Using the grid `grid`, traverse it right x, down y, landing on a character in each subsequent row.
       Start traversing from row number `row_num` at index `index`.
       Place an 'X' on the landing spot (row + slope_y, index + slope_x) if there was originally a '#'(tree) there.
       Otherwise, place an 'O' there if there was originally a '.' (opening) there'''

    try:
        next_row = grid[row_num + slope_y]
        print(f'Starting from row number {row_num} at index {index}')
        #print(f'The next row is row number {row_num + slope_y} because we are descending by {slope_y} rows at a time')
    except IndexError:
        return

    landing_index = index + slope_x
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


def create_filled_grid(grid, X, Y):
    '''Starting with an unfilled grid, begin on row 0, index 0, and fill it out by traversing X over, Y down'''

    # Initialize the new, filled grid with the first row of the old grid since they're the same
    filled = [grid[0]]
    for row_num, _ in enumerate(grid):
        if Y > 1:
            if row_num % 2 == 0:
                index = int(row_num / Y)
                try:
                    next_row = grid[row_num + 1]
                except IndexError:
                    continue
                filled.append(next_row)
                next_next_row = right_x_down_y(grid, row_num, index, X, Y)
                filled.append(next_next_row)
            else:
                continue
        else:
            index = row_num * X
            next_row = right_x_down_y(grid, row_num, index, X, Y)
            if next_row:
                filled.append(next_row)

    return filled


def count_trees(filled_grid):
    '''Once a grid is filled in, we can use this function to count the number of "trees" (X characters)'''
    flattened_grid = [item for sublist in filled_grid for item in sublist]
    char_count = Counter(flattened_grid)
    num_trees = char_count['X']

    return num_trees


def usage():
    '''Print the usage of this script so args can be used'''
    print('python3 day3_part2.py <SLOPE_X> <SLOPE_Y>')
    print('    SLOPE_X and SLOPE_Y are the x and y components of the toboggan slope')


def main():
    try:
        input_file = sys.argv[3]
        if input_file == 'test':
            input_file = 'test_input.txt'
        else:
            raise IndexError
    except IndexError:
        input_file = 'input.txt'

    try:
        slope_x = int(sys.argv[1])
        slope_y = int(sys.argv[2])
    except IndexError:
        usage()
        sys.exit(1)

    grid = read_input(input_file)

    rows = len(grid)
    min_width = find_min_grid_width(rows, slope_x, slope_y)

    rep_grid = construct_repeated_grid(grid, min_width, slope_x, slope_y)
    filled_grid = create_filled_grid(rep_grid, slope_x, slope_y)

    for row in filled_grid:
        print(row)

    num_trees = count_trees(filled_grid)
    print(f'ANSWER: the number of trees is {num_trees}')


if __name__ == '__main__':
    main()
