import sys
from itertools import combinations


def usage(err=None):
    msg = "python3 day08_part1.py <INPUT_FILE> <PAST_N>"
    if err:
        raise SystemExit(msg + f"\n{err}")
    else:
        raise SystemExit(msg)


def read_input():
    try:
        file_name = sys.argv[1]
        past_n = int(sys.argv[2])
        with open(file_name, "r") as inp:
            puzzle_input = inp.read().strip().split("\n")
            return ([int(x) for x in puzzle_input], past_n)
    except (IndexError, ValueError):
        usage()
    except FileNotFoundError as fnfe:
        usage(fnfe)


def get_combos(xmas, num, past_n):
    """Get all combinations of length `num` of the previous `past_n` numbers in `xmas`."""
    relevant = xmas[:past_n]
    combos = [c for c in combinations(relevant, num)]
    return sorted(combos, key=lambda x: x[0])


def single_step(puz, num, past_n):
    combos = get_combos(puz[:past_n], num, past_n)
    sums = [sum(c) for c in combos]
    current = puz[past_n]
    if current not in sums:
        print(f'Found number {current} not in sums.')
        zipped = [z for z in zip(combos, sums)]
        print('\n'.join([str(z) for z in zipped]))
        return current
    else:
        print(f'{current} in sums.')
        return single_step(puz[1:], num, past_n)


def main():
    puz, past_n = read_input()
    # combos = get_combos(puz, 2, 5)
    # print('\n'.join([str(x) for x in combos]))
    answer = single_step(puz, 2, past_n)
    print(answer)


if __name__ == "__main__":
    main()
