#!/usr/bin/env python

def read_input():
    with open('input.txt', 'r') as f:
        puzzle_input = [line.rstrip() for line in f]
    return puzzle_input


def part_1(puzzle_input):
    """
    >>> part_1(['dabAcCaCBAcCcaDA'])
    10
    """
    polymer = puzzle_input[0]
    count = 0
    while count < len(polymer) - 1:
        unit = polymer[count]
        next_unit = polymer[count + 1]
        if unit.lower() == next_unit.lower() and unit != next_unit:
            polymer = polymer[:count] + polymer[count + 2:]
            if count > 0:
                count -= 1
        else:
            count += 1
    return len(polymer)


def part_2(puzzle_input):
    pass

def main():
    puzzle_input = read_input()
    print('Answer for Part 1 is:', part_1(puzzle_input))
    print('Answer for Part 2 is:', part_2(puzzle_input))


if __name__ == '__main__':
    main()
