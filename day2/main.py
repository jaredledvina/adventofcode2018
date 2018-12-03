#!/usr/bin/env python
def read_input():
    with open('input.txt', 'r') as f:
        puzzle_input = [line.rstrip() for line in f]
    return puzzle_input


def count_repeats(text, count):
    """
    >>> count_repeats('abcdefg', 2)
    []
    >>> count_repeats('aabbccd', 2)
    ['a', 'b', 'c']
    >>> count_repeats('aaabbccddd', 3)
    ['a', 'd']
    """

    repeats = []
    for letter in set(text):
        if text.count(letter) == count:
            repeats.append(letter)
    return sorted(repeats)


def part_1(puzzle_input):
    """
    >>> part_1(['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab'])
    12
    """
    total_doubles = 0
    total_triples = 0
    for line in puzzle_input:
        if count_repeats(line, 2):
            total_doubles += 1
        if count_repeats(line, 3):
            total_triples += 1
    return total_doubles * total_triples


def part_2(puzzle_input):
    """
    >>> part_2(['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz'])
    fgij
    """


def main():
    puzzle_input = read_input()
    print('Answer for Part 1 is:', part_1(puzzle_input))
    print('Answer for Part 2 is:', part_2(puzzle_input))


if __name__ == '__main__':
    main()
