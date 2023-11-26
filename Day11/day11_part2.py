import sys
from copy import deepcopy
from typing import List, Tuple


def usage() -> None:
    """Tell the user how to run the script."""
    raise SystemExit("USAGE: python3 day11_part1.py <INPUT_FILE>")


def read_input(name: str = "sample_input.txt") -> List[str]:
    """Read the input file and return list of lines."""
    try:
        with open(name, "r") as p:
            puz = [list(x) for x in p.read().strip().split("\n")]
            return puz
    except (FileNotFoundError, PermissionError):
        usage()


def search_diagonal(pos: Tuple[int, int], grid: List[str]) -> List[str]:
    """Find all diagonally-visible seats."""
    x, y = pos
    print(f'Searching for visible seats for tile at ({x}, {y})')
    diag_up_left = None
    straight_up = None
    diag_up_right = None
    straight_left = None
    diag_down_left = None
    straight_down = None
    diag_down_right = None
    straight_right = None
    # Look diagonally up and left
    while True:
        try:
            x -= 1
            y -= 1
            print(f"Diag up-left: searching at coordinate ({x}, {y})")
            if any([coord < 0 for coord in [x, y]]):
                raise IndexError
            diag_up_left = grid[x][y]
            if diag_up_left in ("#", "L"):
                print(f"Finished with diag up-left {str(diag_up_left)}")
                break
        except IndexError:
            print(f"Out of bounds, finished with diag up-left {str(diag_up_left)}")
            break

    # Look straight up
    x, y = pos
    while True:
        try:
            x -= 1
            print(f"Straight up: searching at coordinate ({x}, {y})")
            if any([coord < 0 for coord in [x, y]]):
                raise IndexError
            straight_up = grid[x][y]
            if straight_up in ("#", "L"):
                print(f"Finished with straight up {str(straight_up)}")
                break
        except IndexError:
            print(f"Out of bounds, finished with straight up {str(straight_up)}")
            break

    # Look diagonally up and right
    x, y = pos
    while True:
        try:
            x -= 1
            y += 1
            print(f"Diag up right: searching at coordinate ({x}, {y})")
            if y >= len(grid[0]) or x < 0:
            # if any([coord < 0 for coord in [x, y]]):
                raise IndexError
            diag_up_right = grid[x][y]
            if diag_up_right in ("#", "L"):
                print(f"Finished with diag up right: {str(diag_up_right)}")
                break
        except IndexError:
            print(f"Out of bounds, finished with diag up-right {str(diag_up_right)}")
            break

    # Look straight left
    x, y = pos
    while True:
        try:
            y -= 1
            print(f"Straight left: searching at coordinate ({x}, {y})")
            if any([coord < 0 for coord in [x, y]]):
                raise IndexError
            straight_left = grid[x][y]
            if straight_left in ("#", "L"):
                print(f"Finished with straight left: {str(straight_left)}")
                break
        except IndexError:
            print(f"Out of bounds, finished with straight left {str(straight_left)}")
            break

    # Look diagonally down and left
    x, y = pos
    while True:
        try:
            x += 1
            y -= 1
            print(f"Diag down left: searching at coordinate ({x}, {y})")
            if x >= len(grid[0]) or y < 0:
            # if any([coord < 0 for coord in [x, y]]):
                raise IndexError
            diag_down_left = grid[x][y]
            if diag_down_left in ("#", "L"):
                print(f"Finished with diag down left: {str(diag_down_left)}")
                break
        except IndexError:
            print(f"Out of bounds, finished with diag down left {str(diag_down_left)}")
            break

    # Look straight down
    x, y = pos
    while True:
        try:
            x += 1
            print(f"Straight down: searching at coordinate ({x}, {y})")
            if x >= len(grid[0]) or y < 0:
            # if any([coord < 0 for coord in [x, y]]):
                raise IndexError
            straight_down = grid[x][y]
            if straight_down in ("#", "L"):
                print(f"Finished with straight down: {str(straight_down)}")
                break
        except IndexError:
            print(f"Out of bounds, finished with straight down {str(straight_down)}")
            break

    # Look diagonally down and right
    x, y = pos
    while True:
        try:
            x += 1
            y += 1
            print(f"Diag down right: searching at coordinate ({x}, {y})")
            if any([coord >= len(grid[0]) for coord in [x, y]]):
            # if any([coord < 0 for coord in [x, y]]):
                raise IndexError
            diag_down_right = grid[x][y]
            if diag_down_right in ("#", "L"):
                print(f"Finished with diag down right: {str(diag_down_right)}")
                break
        except IndexError:
            print(f"Out of bounds, finished with diag down right {str(diag_down_right)}")
            break

    # Look straight right
    x, y = pos
    while True:
        try:
            y += 1
            print(f"Straight right: searching at coordinate ({x}, {y})")
            if y >= len(grid[0]):
            # if any([coord < 0 for coord in [x, y]]):
                raise IndexError
            straight_right = grid[x][y]
            if straight_right in ("#", "L"):
                print(f"Finished with straight right: {str(straight_right)}")
                break
        except IndexError:
            print(f"Out of bounds, finished with straight right {str(straight_right)}")
            break
    all_coords = [
        x
        for x in [
            diag_up_left,
            straight_up,
            diag_up_right,
            straight_left,
            diag_down_left,
            straight_down,
            diag_down_right,
            straight_right,
        ]
        if x is not None
    ]
    return all_coords


def find_adjacent(pos: Tuple[int, int], grid: List[str]) -> Tuple[str, List[str]]:
    """Find all adjacent tiles to `pos`."""

    def get_above_left(grid):
        return grid[pos[0] - 1][pos[1] - 1]

    def get_above_mid(grid):
        return grid[pos[0] - 1][pos[1]]

    def get_above_right(grid):
        return grid[pos[0] - 1][pos[1] + 1]

    def get_left(grid):
        return grid[pos[0]][pos[1] - 1]

    def get_self(grid):
        return grid[pos[0]][pos[1]]

    def get_right(grid):
        return grid[pos[0]][pos[1] + 1]

    def get_below_left(grid):
        return grid[pos[0] + 1][pos[1] - 1]

    def get_below_mid(grid):
        return grid[pos[0] + 1][pos[1]]

    def get_below_right(grid):
        return grid[pos[0] + 1][pos[1] + 1]

    def validate_adjacent(adj):
        """Ensure no values are None."""
        if any([a is None for a in adj]):
            raise SystemExit(f"Found None in adjacent: {adj}")

    grid_w = len(grid[0])
    grid_h = len(grid)
    self = get_self(grid)
    if pos[0] == 0:
        # We're on the top row
        if pos[1] == 0:
            # We're in the top-left corner
            right = get_right(grid)
            below_mid = get_below_mid(grid)
            below_right = get_below_right(grid)
            adj = [right, below_mid, below_right]
            validate_adjacent(adj)
            return (self, adj)
        elif pos[1] == grid_w - 1:
            # We're in the top-right corner
            left = get_left(grid)
            below_left = get_below_left(grid)
            below_mid = get_below_mid(grid)
            adj = [left, below_left, below_mid]
            validate_adjacent(adj)
            return (self, adj)
        else:
            # We're somewhere in the top-middle, horizontally
            # This guarantees us 5 adjacent tiles
            left = get_left(grid)
            below_left = get_below_left(grid)
            below_mid = get_below_mid(grid)
            below_right = get_below_right(grid)
            right = get_right(grid)
            adj = [left, below_left, below_mid, below_right, right]
            validate_adjacent(adj)
            return (self, adj)
    elif pos[0] == grid_h - 1:
        # We're on the bottom row
        if pos[1] == 0:
            # We're in the bottom-left corner
            above_mid = get_above_mid(grid)
            above_right = get_above_right(grid)
            right = get_above_right(grid)
            adj = [above_mid, above_right, right]
            validate_adjacent(adj)
            return (self, adj)
        elif pos[1] == grid_w - 1:
            # We're in the bottom-right corner
            above_left = get_above_left(grid)
            above_mid = get_above_mid(grid)
            left = get_left(grid)
            adj = [above_left, above_mid, left]
            validate_adjacent(adj)
            return (self, adj)
        else:
            # We're somewhere in the bottom-middle, horizontally
            # This guarantees us 5 tiles
            left = get_left(grid)
            above_left = get_above_left(grid)
            above_mid = get_above_mid(grid)
            above_right = get_above_right(grid)
            right = get_right(grid)
            adj = [left, above_left, above_mid, above_right, right]
            validate_adjacent(adj)
            return (self, adj)
    if pos[1] == 0:
        # We're on the leftmost column, but not in a corner
        # That means we have 5 adjacent tiles
        above_mid = get_above_mid(grid)
        above_right = get_above_right(grid)
        right = get_right(grid)
        below_mid = get_below_mid(grid)
        below_right = get_below_right(grid)
        adj = [above_mid, above_right, right, below_mid, below_right]
        validate_adjacent(adj)
        return (self, adj)
    elif pos[1] == grid_w - 1:
        # We're on the rightmost column, but not in a corner
        # That means we have 5 adjacent tiles
        above_mid = get_above_mid(grid)
        above_left = get_above_left(grid)
        left = get_left(grid)
        below_mid = get_below_mid(grid)
        below_left = get_below_left(grid)
        adj = [above_mid, above_left, left, below_mid, below_left]
        validate_adjacent(adj)
        return (self, adj)

    # If none of the above, we're guaranteed to have 8 adjacent tiles
    above_mid = get_above_mid(grid)
    above_right = get_above_right(grid)
    right = get_right(grid)
    below_mid = get_below_mid(grid)
    below_right = get_below_right(grid)
    above_left = get_above_left(grid)
    left = get_left(grid)
    below_left = get_below_left(grid)
    adj = [
        above_left,
        above_mid,
        above_right,
        left,
        right,
        below_left,
        below_mid,
        below_right,
    ]
    validate_adjacent(adj)
    return (self, adj)


def find_tile_val(tile: str, adjacent: List[str]) -> str:
    """Decide whether to update a tile's value based on adjacent tiles."""
    # print(f'Tile is "{tile}", adjacent is {", ".join([str(x) for x in adjacent])}')
    if tile == ".":
        # Current tile is not a seat, do nothing
        # print('Nothing to do, returning "."')
        return tile

    if tile == "L":
        # Current seat is empty, check surrounding seats
        if adjacent.count("#") == 0:
            # print('Found no occupied adjacent seats, returning "#"')
            return "#"
        else:
            # print('At least one adjacent seat occupied, returning "L"')
            return "L"

    if tile == "#":
        # Current seat is occupied, check surrounding seats
        if adjacent.count("#") >= 5:
            # print('Occupied adjacent seats >= 5, returning "L"')
            return "L"
        else:
            # print('Occupied adjacent seats < 5, returning "#"')
            return "#"
    else:
        raise SystemExit(f'Tile "{str(tile)}" was not one of (".", "L", "#")')


def step(grid: List[str], counter: int = 0) -> List[str]:
    """Take one step forward in the seating simulation."""
    new_grid = deepcopy(grid)
    for i in range(len(grid)):
        # Iterate over each row
        for j in range(len(grid[0])):
            # Iterate over each column
            # print(f'Checking tile in row {str(i).zfill(2)}, column {str(j).zfill(2)}')
            tile, adjacent = find_adjacent((i, j), grid)
            new_grid[i][j] = find_tile_val(tile, adjacent)

    if new_grid == grid:
        return (new_grid, counter)
    else:
        print_grid(new_grid)
        counter += 1
        return step(new_grid, counter)


def print_grid(grid: List[str]) -> None:
    """Print the grid for visualization."""
    for row in grid:
        row_joined = "".join(row)
        print(row_joined)

    print("\n")


def count_occupied_seats(final_form: List[str]) -> int:
    """After the grid stops changing, return a tally of occupied seats."""
    return sum([row.count("#") for row in final_form])


def main():
    try:
        try:
            input_file = sys.argv[1]
            grid = read_input(input_file)
        except IndexError:
            grid = read_input()
        print_grid(grid)
        bunch_of_coords = search_diagonal((9, 5), grid)
        print(f'Coordinates: {", ".join([str(x) for x in bunch_of_coords])}')
        # final_form, total_steps = step(grid)
        # occupied_seats = count_occupied_seats(final_form)
        # print(f'Ran for {total_steps} rounds')
        # print(f'ANSWER: {occupied_seats}')
    except BrokenPipeError:
        sys.exit(0)


if __name__ == "__main__":
    main()
