import sys

def open_input(input_file):
    '''open the input file'''
    try:
        with open(input_file, 'r') as inp:
            inp_data = inp.read().strip()
            inp_ls = [int(x) for x in inp_data.split('\n') if x != '']
    except FileNotFoundError:
        print('input file not found')
        sys.exit(1)
    except PermissionError:
        print('input file found, but read permission is not set')
        sys.exit(1)
    else:
        return inp_ls


def sums_to_x(inp_ls, x):
    '''Given an input list `inp_ls` of integers, return a tuple of the two that add to x'''
    #print(f'The length of the input list given to `sums_to_x` is {len(inp_ls)}')
    first = inp_ls[0]
    for num in inp_ls[1:]:
        if first + num == x:
            return (first, num)
    if len(inp_ls[1:]) > 3:
        return sums_to_x(inp_ls[1:], x)
    else:
        return None


def main():
    numbers = open_input('input.txt')
    num1, num2 = sums_to_x(numbers, 2020)
    print(f'The two numbers that add to 2020 are {num1} and {num2}')
    print(f'ANSWER: the product of {num1} and {num2} is {num1 * num2}')


if __name__ == '__main__':
    main()
