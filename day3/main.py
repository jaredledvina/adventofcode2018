#!/usr/bin/env python

import re

def read_input():
    with open('input.txt', 'r') as f:
        puzzle_input = [line.rstrip() for line in f]
    return puzzle_input


def parse_input(puzzle_input):
    """
    Parses out this fucked up format and returns the vertices for each point
    of the claimed rectangle
    >>> parse_input(['#990 @ 586,641: 15x12'])
    {990: [(586, 641), (601, 641), (586, 653), (601, 653)]}
    """
    parsed_input = {}
    for claim in puzzle_input:
        parsed_claim = re.search(r'^\#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$', claim)
        parsed_input[int(parsed_claim[1])] = [
            (int(parsed_claim[2]), int(parsed_claim[3])),
            (int(parsed_claim[2]) + int(parsed_claim[4]), int(parsed_claim[3])),
            (int(parsed_claim[2]), int(parsed_claim[3]) + int(parsed_claim[5])),
            (int(parsed_claim[2]) + int(parsed_claim[4]), int(parsed_claim[3]) + int(parsed_claim[5]))]
    return parsed_input


def count_claims(claim_corners):
    claim_points = []
    for y_point in range(min([y[1] for y in claim_corners]), max([y[1] for y in claim_corners])):
        for x_point in range(min([x[0] for x in claim_corners]), max([x[0] for x in claim_corners])):
            claim_points.append((x_point, y_point))
    return claim_points


def part_1(puzzle_input):
    """
    >>> part_1(['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2'])
    4
    """
    parsed_puzzle_input = parse_input(puzzle_input)
    claimed_squares = {}
    for claim, points in parsed_puzzle_input.items():
        claim_squares = count_claims(points)
        for square in claim_squares:
            if square in claimed_squares:
                claimed_squares[square] += 1
            else:
                claimed_squares[square] = 1
    return len([point for point in claimed_squares if claimed_squares[point] > 1])


def part_2(puzzle_input):
    """
    >>> part_2(['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2'])
    3
    """
    parsed_puzzle_input = parse_input(puzzle_input)
    per_claim_squares = {}
    overall_claimed_squares = {}
    for claim, points in parsed_puzzle_input.items():
        claim_squares = count_claims(points)
        per_claim_squares[claim] = claim_squares
        for square in claim_squares:
            if square in overall_claimed_squares:
                overall_claimed_squares[square] += 1
            else:
                overall_claimed_squares[square] = 1

    single_squares = []
    for square in overall_claimed_squares.keys():
        if overall_claimed_squares[square] == 1:
            single_squares.append(square)
    final = per_claim_squares.copy()
    for claim, square in per_claim_squares.items():
        for square in square:
            if square in single_squares:
                pass
            else:
                final.pop(claim)
                break
    return list(final.keys())[0]


def main():
    puzzle_input = read_input()
    print('Answer for Part 1 is:', part_1(puzzle_input))
    print('Answer for Part 2 is:', part_2(puzzle_input))


if __name__ == '__main__':
    main()
