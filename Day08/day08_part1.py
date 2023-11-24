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


def run_instr(index, page, acc, seen=None):
    """Run instructions."""
    print(f"Current index: {index}")
    if seen is None:
        print("List of seen lines is empty. Initializing it.")
        seen = set()
    else:
        if index in seen:
            print(f"We've already seen index {index}. Exiting.")
            return acc
    spl = page[index].split()
    instr = spl[0]
    if instr == "nop":
        print("Found nop. Skipping.")
        if len(page) <= index + 1:
            print("Can't go to next instruction. Page is not long enough.")
            return acc
        else:
            seen.add(index)
            print(f"Added index {index} to seen.")
            return run_instr(index + 1, page, acc, seen)
    elif instr == "acc":
        print("Found acc. Accumulating...")
        num = int(spl[1].strip().replace('+', ''))
        print(f"\t acc num: {num}")
        print(f"Added index {index} to seen.")
        seen.add(index)
        print(f"\told acc: {acc}, new acc: {acc + num}")
        acc += num
        return run_instr(index + 1, page, acc, seen)
    elif instr == "jmp":
        loc = int(spl[1].strip().replace('+', ''))
        print(f"Found jmp. Jumping {loc} lines to index {index + loc}")
        return run_instr(index + loc, page, acc, seen)


def main():
    page = read_input('puzzle_input.txt')
    acc = 0
    acc = run_instr(0, page, acc)
    print(f'ANSWER: {acc}')


if __name__ == '__main__':
    main()
