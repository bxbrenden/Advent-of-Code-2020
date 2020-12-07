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


def bisect_rows(boarding_pass, bp_lower=0, bp_upper=128):
    '''Bisect the rows of a boarding pass, i.e. the first 7 characters (either F or B).
       Return the row number for the seat specified by the boarding pass.
       `bp_upper` is the upper bound (exclusive) of the current boarding pass section, and
       `bp_lower` is the lower bound (inclusive).'''

    print(f'The whole boarding pass is now: {boarding_pass}')

    # get the first character
    section = boarding_pass[0]
    print(f'The section is now {section}')
    if len(boarding_pass) > 1:
        if section == 'F':
            # the upper bound (exclusive) is (`bp_upper` divided by two) + (`bp_lower` divided by two)
            upper_bound = (bp_upper / 2) + (bp_lower / 2)
            # the lower bound (inclusive) is just `bp_lower` itself
            lower_bound = bp_lower
            print(f'The lower bound is {int(lower_bound)}, and the upper bound is {int(upper_bound)}')
            return bisect_rows(boarding_pass[1:], lower_bound, upper_bound)
        elif section == 'B':
            # the upper bound (exclusive) is just `bp_upper` itself
            upper_bound = bp_upper
            # the lower bound (inclusive) is
            lower_bound = ((bp_upper - bp_lower) / 2) + bp_lower
            print(f'The lower bound is {int(lower_bound)}, and the upper bound is {int(upper_bound)}')
            return bisect_rows(boarding_pass[1:], lower_bound, upper_bound)
    else:
        if section == 'F':
            row = int(bp_lower)
            print(f'The row for this boarding pass is: {row}')
            return row
        elif section == 'B':
            row = int(bp_upper - 1)
            print(f'The row for this boarding pass is: {row}')
            return row


def bisect_columns(columns, bp_lower=0, bp_upper=8):
    '''Get the column number of the seat based on the final 3 chars (all 'L' or 'R')'''
    section = columns[0]
    if len(columns) > 1:
        if section == 'L':
            lower_bound = bp_lower
            upper_bound = (bp_upper / 2) + (bp_lower / 2)
            print(f'The lower bound is now {lower_bound}, and the upper bound is now {upper_bound}')
            return bisect_columns(columns[1:], lower_bound, upper_bound)
        elif section == 'R':
            upper_bound = bp_upper
            lower_bound = ((bp_upper - bp_lower) / 2) + bp_lower
            print(f'The lower bound is now {lower_bound}, and the upper bound is now {upper_bound}')
            return bisect_columns(columns[1:], lower_bound, upper_bound)
    else:
        if section == 'L':
            column = int(bp_lower)
            print(f'The column for this boarding pass is {column}')
            return column
        elif section == 'R':
            column = int(bp_upper - 1)
            print(f'The column for this boarding pass is {column}')
            return column


def main():
    input_file = 'input.txt'
    boarding_passes = read_input(input_file)
    for bp in boarding_passes:
        print(bp)


if __name__ == '__main__':
    main()
