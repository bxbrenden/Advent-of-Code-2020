from day5_part1 import read_input
import sys


def main():
    input_file = 'input.txt'
    boarding_passes = read_input(input_file)

    for bp in boarding_passes:
        print(bp)


if __name__ == '__main__':
    main()
