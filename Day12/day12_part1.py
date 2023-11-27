from enum import Enum
from typing import List
import sys


class Direction(Enum):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3


class Ship:
    def __init__(self, directions):
        self.directions = directions
        self.facing = Direction.EAST
        self.emoji = "➡️"
        self.east = 0
        self.south = 0
        self.west = 0
        self.north = 0
        self.steps = 0
        print(self)

    def __str__(self):
        info = f'🚢{self.emoji}\n'
        info += f'N={self.north}\n'
        info += f'E={self.east}\n'
        info += f'S={self.south}\n'
        info += f'W={self.west}\n'
        return info

    def engage(self):
        for direction in self.directions:
            self.navigate(direction)
        return self.manhattan()

    def set_emoji(self):
        match self.facing:
            case Direction.EAST:
                self.emoji = '➡️'
            case Direction.SOUTH:
                self.emoji = '⬇️'
            case Direction.WEST:
                self.emoji = '⬅️'
            case Direction.NORTH:
                self.emoji = '⬆️'

    def navigate(self, instr):
        """Given an instruction, update the ship's location and orientation."""
        direction = instr[0]
        magnitude = int(instr[1:])
        print(f'Direction: {direction}, Magnitude: {magnitude}')
        match direction:
            case 'E':
                self.east += magnitude
            case 'S':
                self.south += magnitude
            case 'W':
                self.west += magnitude
            case 'N':
                self.north += magnitude
            case 'F':
                match self.facing:
                    case Direction.EAST:
                        self.east += magnitude
                    case Direction.SOUTH:
                        self.south += magnitude
                    case Direction.WEST:
                        self.west += magnitude
                    case Direction.NORTH:
                        self.north += magnitude
            case 'R':
                self.facing = Direction(int((self.facing.value + (magnitude / 90)) % 4))
            case 'L':
                self.facing = Direction(int((self.facing.value - (magnitude / 90)) % 4))
            case _:
                raise SystemExit(f'Unexpected case: {direction}')
        self.steps += 1
        self.set_emoji()
        print(self)

    def summarize(self):
        print(f'Total steps taken: {self.steps}')

    def manhattan(self):
        man = abs(self.east - self.west) + abs(self.north - self.south)
        return f'Manhattan Dist. from Start: {man}'


def usage():
    raise SystemExit('USAGE: python3 day12_part1.py [INPUT_FILE]')


def read_input(filename: str) -> List[str]:
    """Read the input file."""
    try:
        with open(filename, 'r') as inp:
            puzzle = inp.read().strip().split('\n')
            return puzzle
    except (FileNotFoundError, PermissionError):
        usage()


def main():
    try:
        input_file = sys.argv[1]
    except IndexError:
        input_file = "sample_input.txt"

    directions = read_input(input_file)
    ship = Ship(directions)
    final = ship.engage()
    ship.summarize()
    print(final)


if __name__ == '__main__':
    main()
