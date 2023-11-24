from typing import List


def read_input(input_file):
    """Read the input file and return it in digestible chunks"""
    try:
        with open(input_file, "r") as inp:
            input_str = inp.read().strip()
            input_list = [int(n) for n in input_str.split("\n")]
            return sorted(input_list)
    except (FileNotFoundError, PermissionError) as err:
        raise SystemExit(
            f"Failed to read input file {input_file} with exception:\n{err}"
        )


def find_joltage_diffs(puz: List[int], three_diffs: int = 0, one_diffs: int = 1) -> int:
    try:
        new_diff = puz[1] - puz[0]
        print(f'Diff: {puz[1]} - {puz[0]} = {new_diff}')
        if new_diff == 1:
            print(f'one diffs += 1, now at {one_diffs + 1}')
            one_diffs += 1
        elif new_diff == 3:
            print(f'three diffs += 1, now at {three_diffs + 1}')
            three_diffs += 1
        if len(puz) <= 2:
            print(f'Adding one more to three_diffs value {three_diffs}')
            three_diffs += 1
            print(f'Final one diffs: {one_diffs}')
            print(f'Final three diffs: {three_diffs}')
            return one_diffs * three_diffs
        else:
            return find_joltage_diffs(puz[1:], three_diffs, one_diffs)
    except IndexError:
        raise SystemExit('This is unexpected...')


def main():
    puz = read_input("puzzle_input.txt")
    print("\n".join([str(p) for p in puz]))
    answer = find_joltage_diffs(puz)
    print(f'ANSWER: {answer}')


if __name__ == "__main__":
    main()
