from day6_part1 import read_input
import sys


def main():
    input_file = 'test_input.txt'
    questions = read_input(input_file)

    for q in questions:
        print(q + '\n')


if __name__ == '__main__':
    main()
