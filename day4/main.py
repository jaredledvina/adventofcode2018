#!/usr/bin/env python

from collections import OrderedDict
from datetime import datetime, timedelta
import re

def read_input():
    with open('input.txt', 'r') as f:
        puzzle_input = [line.rstrip() for line in f]
    return puzzle_input


def get_schedule(puzzle_input):
    """
    Returns an Ordered Dictionary of the schedule
    """
    schedule = {}
    for entry in puzzle_input:
        timestamp = datetime.strptime(entry[1:17], "%Y-%m-%d %H:%M")
        event = entry[19:]
        schedule[timestamp] = event
    return OrderedDict(sorted(schedule.items(), key=lambda t: t[0]))

def get_guard_schedule(schedule):
    """
    Returns the schedule of each guard
    """
    guard_schedule = {}
    for entry in schedule:
        if 'Guard' in schedule[entry]:
            current_guard = re.search(r'^Guard #(\d+) begins shift$', schedule[entry])[1]
            current_guard_start = entry
            if current_guard not in guard_schedule:
                guard_schedule[current_guard] = {}
        elif 'falls asleep' in schedule[entry]:
            current_guard_sleep = entry
            if current_guard_sleep in guard_schedule[current_guard]:
                guard_schedule[current_guard][current_guard_sleep] += 1
            else:
                guard_schedule[current_guard][current_guard_sleep] = 1
        elif 'wakes up' in schedule[entry]:
            current_guard_wakes = entry
            time_asleep = current_guard_wakes - current_guard_sleep
            sleeping_minute = current_guard_sleep
            for minute in range(0, time_asleep.seconds // 60 - 1):
                sleeping_minute = sleeping_minute + timedelta(0, 60)
                if sleeping_minute in guard_schedule[current_guard]:
                    guard_schedule[current_guard][sleeping_minute] += 1
                else:
                    guard_schedule[current_guard][sleeping_minute] = 1
    return guard_schedule


def condense_guard_schedule(guard_schedule):
    """
    Takes a guard_schedule and condenses it into just minutes
    """
    condensed_guard_schedule = {}
    for guard in guard_schedule:
        condensed_guard_schedule[guard] = {}
        for entry in guard_schedule[guard]:
            if entry.minute in condensed_guard_schedule[guard]:
                condensed_guard_schedule[guard][entry.minute] += 1
            else:
                condensed_guard_schedule[guard][entry.minute] = 1
    return condensed_guard_schedule


def part_1(puzzle_input):
    """
    >>> part_1(['[1518-11-01 00:00] Guard #10 begins shift', '[1518-11-01 00:05] falls asleep', '[1518-11-01 00:25] wakes up', '[1518-11-01 00:30] falls asleep', '[1518-11-01 00:55] wakes up', '[1518-11-01 23:58] Guard #99 begins shift', '[1518-11-02 00:40] falls asleep', '[1518-11-02 00:50] wakes up', '[1518-11-03 00:05] Guard #10 begins shift', '[1518-11-03 00:24] falls asleep', '[1518-11-03 00:29] wakes up', '[1518-11-04 00:02] Guard #99 begins shift', '[1518-11-04 00:36] falls asleep', '[1518-11-04 00:46] wakes up', '[1518-11-05 00:03] Guard #99 begins shift', '[1518-11-05 00:45] falls asleep', '[1518-11-05 00:55] wakes up]'])
    240
    """
    schedule = get_schedule(puzzle_input)
    guard_schedule = get_guard_schedule(schedule)
    condensed_guard_schedule = condense_guard_schedule(guard_schedule)
    sleep = { key: len(value) for key, value in condensed_guard_schedule.items() }
    sleepiest_guard = max(sleep, key=sleep.get)
    sleepiest_minute = max(condensed_guard_schedule[sleepiest_guard], key=condensed_guard_schedule[sleepiest_guard].get)
    return int(sleepiest_guard) * int(sleepiest_minute)



def part_2(puzzle_input):
    pass

def main():
    puzzle_input = read_input()
    print('Answer for Part 1 is:', part_1(puzzle_input))
    print('Answer for Part 2 is:', part_2(puzzle_input))


if __name__ == '__main__':
    main()
