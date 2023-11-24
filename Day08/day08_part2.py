from typing import List


def read_input(input_file):
    """Read the input file and return it in digestible chunks"""
    try:
        with open(input_file, "r") as inp:
            input_str = inp.read().strip()
            input_list = input_str.split("\n")
            return input_list
    except (FileNotFoundError, PermissionError) as err:
        raise SystemExit(
            f"Failed to read input file {input_file} with exception:\n{err}"
        )


def run_instr(index: int, page: List[str], acc: int, seen=None) -> (int, bool):
    """Run instructions.

    Return (acc, terminated) where `acc` is the value of the accumulator and
    `terminated` is a bool indicating whether the execution terminated without
    looping.
    """
    print(f"Current index: {index}")
    if seen is None:
        print("List of seen lines is empty. Initializing it.")
        seen = set()
    else:
        if index in seen:
            print(f"We've already seen index {index}. Exiting.")
            return (acc, False)
    spl = page[index].split()
    instr = spl[0]
    if instr == "nop":
        print("Found nop. Skipping.")
        if len(page) == index + 1:
            print("Can't go to next instruction. Page is not long enough.")
            return (acc, True)
        else:
            seen.add(index)
            print(f"Added index {index} to seen.")
            return run_instr(index + 1, page, acc, seen)
    elif instr == "acc":
        print("Found acc. Accumulating...")
        num = int(spl[1].strip().replace("+", ""))
        print(f"\t acc num: {num}")
        print(f"Added index {index} to seen.")
        seen.add(index)
        print(f"\told acc: {acc}, new acc: {acc + num}")
        acc += num
        next_index = index + 1
        if next_index == len(page):
            print(f"Termination reached by acc. to non-existent index {next_index}")
            return (acc, True)
        return run_instr(next_index, page, acc, seen)
    elif instr == "jmp":
        loc = int(spl[1].strip().replace("+", ""))
        if index + loc == len(page):
            print(f"Termination reached by jump to non-existent index {index + 1}")
            return (acc, True)
        if loc == 0:
            print(f'Loop detected for jmp at index {index}')
            return (acc, False)
        print(f"Found jmp. Jumping {loc} lines to index {index + loc}")
        return run_instr(index + loc, page, acc, seen)


def test_all_replacements(page):
    """Find all combinations of single-substitution nop vs. jmp."""
    # Create list to store all combinations
    pages = []

    # Create list to store indices of relevant instructions
    eligible = []

    for index, line in enumerate(page):
        print(f'Checking line "{line}" at index {index} for nop or jmp.')
        instr = line.split()[0]
        if instr in ["nop", "jmp"]:
            print(f"MATCH FOUND at index {index}")
            eligible.append(index)
    print(
        f'The following lines are replaceable:\n{", ".join([str(e) for e in eligible])}'
    )
    print(f"Total eligible: {len(eligible)}")

    for e in eligible:
        new_page = page.copy()
        sub_line = new_page[e]
        instr = sub_line.split()[0]
        if instr == 'nop':
            sub_line = sub_line.replace('nop', 'jmp', 1)
        elif instr == 'jmp':
            sub_line = sub_line.replace('jmp', 'nop', 1)
        else:
            raise SystemExit(f'Error: found "eligible" value {instr} that is not eligible.')
        new_page[e] = sub_line
        pages.append(new_page)

    for p in pages:
        yield p


def main():
    page = read_input("puzzle_input.txt")
    all_pages = test_all_replacements(page)
    # for p in all_pages:
    #     print('\n'.join(p), '\n')
    for i, p in enumerate(all_pages):
        print(f'Trying page {i + 1}')
        print('Lines for page:\n')
        print('\n'.join(p))
        acc = 0
        acc, term_success = run_instr(0, p, acc)
        if term_success:
            print(f"ANSWER: {acc}. Found in iteration number {i}")
            break


if __name__ == "__main__":
    main()
