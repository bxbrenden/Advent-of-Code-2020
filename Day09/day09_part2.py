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
        # zipped = [z for z in zip(combos, sums)]
        # print('\n'.join([str(z) for z in zipped]))
        return current
    else:
        print(f'{current} in sums.')
        return single_step(puz[1:], num, past_n)


def find_contig(puz, culprit):
    try:
        for n in puz:
            if n > culprit:
                return find_contig(puz[1:], culprit)
            elif n == culprit:
                return find_contig(puz[1:], culprit)
            else:
                indices = []
                s = n
                indices.append((0, puz[0]))
                for r in range(len(puz)):
                    next_val = puz[r + 1]
                    s += next_val
                    if s > culprit:
                        return find_contig(puz[1:], culprit)
                    elif s == culprit:
                        indices.append((r + 1, next_val))
                        return indices
                    else:
                        indices.append((r + 1, next_val))
    except IndexError:
        raise SystemExit('Exceeded list length')


def main():
    puz, past_n = read_input()
    culprit = single_step(puz, 2, past_n)
    print(culprit)
    indices = find_contig(puz, culprit)
    print(indices)
    answers = [t[1] for t in indices]
    assert sum(answers) == culprit
    lower = min(answers)
    upper = max(answers)
    print(f'Lower: {lower}, Upper: {upper}')
    print(f'ANSWER: {lower + upper}')


if __name__ == "__main__":
    main()
