#!/usr/bin/env python

def read_input():
    with open('input.txt', 'r') as f:
        puzzle_input = [line.rstrip() for line in f]
    return puzzle_input


def react(polymer):
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
    return polymer


def part_1(puzzle_input):
    """
    >>> part_1(['dabAcCaCBAcCcaDA'])
    10
    """
    polymer = puzzle_input[0]
    reacted = react(polymer)
    return len(reacted)


def part_2(puzzle_input):
    """
    >>> part_2(['dabAcCaCBAcCcaDA'])
    4
    """
    polymer = puzzle_input[0]
    letters = [chr(pair) for pair in range(ord('a'),ord('z')+1)]
    range(0, len(polymer), 2)
    shortest = 100000
    for letter in letters:
        cleaned = [unit for unit in polymer if unit != letter and unit != letter.upper()]
        reacted = react(cleaned)
        if shortest and len(reacted) < shortest:
            shortest = len(reacted)
    return shortest

def main():
    puzzle_input = read_input()
    print('Answer for Part 1 is:', part_1(puzzle_input))
    print('Answer for Part 2 is:', part_2(puzzle_input))


if __name__ == '__main__':
    main()
