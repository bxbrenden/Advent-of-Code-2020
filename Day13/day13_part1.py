from typing import List, Tuple
import sys


def usage() -> None:
    """Tell the user how to run the program."""
    raise SystemExit("USAGE: python3 day13_part1.py [INPUT_FILE]")


def read_input(input_file: str) -> Tuple[int, List[int]]:
    """Read the input data from a file; return list of strings."""
    try:
        with open(input_file, "r") as inp:
            puzzle = inp.read().strip().split("\n")
            earliest = int(puzzle[0])
            schedule = [int(n) for n in puzzle[1].split(",") if n != "x"]
            return (earliest, schedule)
    except (FileNotFoundError, PermissionError):
        usage()


def get_next_bus(earliest: int, schedule: Tuple[int, List[int]]) -> List[Tuple[int, int]]:
    """Given earliest and schedule, return bus num. for next-available bus."""
    possible = []
    for num in schedule:
        next_bus = ((earliest // num) * num) + num
        possible.append((num, next_bus))

    soonest_bus_index = 0
    smallest_diff = 0
    for i, p in enumerate(possible):
        if i == 0:
            smallest_diff = abs(earliest - p[1])
            soonest_bus_index = i
            continue
        new_diff = earliest - p[1]
        if abs(new_diff) < smallest_diff:
            soonest_bus_index = i
            smallest_diff = new_diff

    return (possible[soonest_bus_index])


def main():
    try:
        input_file = sys.argv[1]
    except IndexError:
        input_file = "sample_input.txt"
    earliest, schedule = read_input(input_file)
    next_bus, nearest_time = get_next_bus(earliest, schedule)
    print(f"The soonest bus for timestamp {earliest} is the number {next_bus} bus at time {nearest_time}")
    print(f'ANSWER: {(nearest_time - earliest) * next_bus}')


if __name__ == "__main__":
    main()
