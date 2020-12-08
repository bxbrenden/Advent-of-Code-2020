from day5_part1 import read_input, calc_seat_id
import sys


def bp_to_bin(bp):
    '''Convert a boarding pass to a binary number'''
    binary = []
    for char in list(bp):
        if char == 'F' or char == 'L':
            num = '0'
        elif char == 'B' or char == 'R':
            num = '1'
        binary.append(num)

    binary = int(''.join(binary), 2)
    print(f'Converted boarding pass {bp} to binary {str(binary)}')

    return binary


def compare_ranges(bins):
    '''Compare a range of ints generated within this function. Return the missing number'''
    lower = min(bins)
    upper = max(bins) + 1

    int_range = [n for n in range(lower, upper)]

    for index, binary in enumerate(bins):
        r = int_range[index]
        #print(f'Binary: {binary}, Int: {r}')
        if str(binary) == str(r):
            print(f'Still matching. binary: {binary}, int: {r}')
            continue
        else:
            print(f'NOT MATCHING! binary: {binary}, int: {r}')
            print(f'Found missing number: {r}')
            return r


def int_to_bin_to_bp(num):
    '''Take an integer and turn it into binary. Turn that binary into a boarding pass'''
    b_list = list(bin(num))[2:]

    row = []
    for b in b_list[:7]:
        if b == '0':
            r = 'F'
        elif b == '1':
            r = 'B'
        row.append(r)

    column = []
    for b in b_list[7:]:
        if b == '0':
            c = 'L'
        elif b == '1':
            c = 'R'
        column.append(c)

    bp = ''.join(row) + ''.join(column)
    print(f'Converted integer {num} into boarding pass {bp}')
    return bp


def main():
    input_file = 'input.txt'
    boarding_passes = read_input(input_file)

    bins = []
    for bp in boarding_passes:
        binary = bp_to_bin(bp)
        bins.append(binary)

    bins.sort()

    missing = compare_ranges(bins)
    missing_pass = int_to_bin_to_bp(missing)

    missing_seat_id = calc_seat_id(missing_pass)

if __name__ == '__main__':
    main()
