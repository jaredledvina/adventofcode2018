#!/usr/bin/env python
def read_input():
    with open('input.txt', 'r') as f:
        puzzle_input = [int(line.rstrip().strip('+')) for line in f]
    return puzzle_input

def part_2(puzzle_input):
    """
    >>> part_2([1, -1])
    0
    >>> part_2([3, 3, 4, -2, -4])
    10
    >>> part_2([-6, 3, 8, 5, -6])
    5
    >>> part_2([7, 7, -2, -7, -4])
    14
    """
    current_frequency = 0
    iteration = 0
    list_end_index = len(puzzle_input) - 1
    results = set((current_frequency,))
    count = 0
    while True:
        current_frequency += puzzle_input[iteration]
        if current_frequency in results:
            return current_frequency
        results.add(current_frequency)
        iteration += 1
        if iteration > list_end_index:
            iteration = 0
        count += 1


def main():
    puzzle_input = read_input()
    print('Answer for Part 1 is:', sum(puzzle_input))
    print('Answer for Part 2 is:', part_2(puzzle_input))



if __name__ == '__main__':
    main()

