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


def sums_to_2020(inp_ls):
    '''Given an input list `inp_ls` of integers, return a tuple of the two that add to 2020'''
    first = inp_ls[0]
    for num in inp_ls[1:]:
        if first + num == 2020:
            return (first, num)
    return sums_to_2020(inp_ls[1:])


def main():
    numbers = open_input('input.txt')
    num1, num2 = sums_to_2020(numbers)
    print(f'The two numbers that add to 2020 are {num1} and {num2}')
    print(f'ANSWER: the product of {num1} and {num2} is {num1 * num2}')


if __name__ == '__main__':
    main()
