#!/usr/bin/env python

from collections import OrderedDict, Counter, defaultdict
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
    guard_schedule = defaultdict(Counter)
    for entry in schedule:
        if 'Guard' in schedule[entry]:
            current_guard = re.search(r'^Guard #(\d+) begins shift$', schedule[entry])[1]
            current_guard_start = entry
        elif 'falls asleep' in schedule[entry]:
            current_guard_sleep = entry
        elif 'wakes up' in schedule[entry]:
            current_guard_wakes = entry
            sleeping_minutes = []
            for minute in range(current_guard_sleep.minute, current_guard_wakes.minute):
                sleeping_minutes.append(minute % 60 )
            guard_schedule[current_guard].update(Counter(sleeping_minutes))
    return guard_schedule


def part_1(puzzle_input):
    """
    >>> part_1(['[1518-11-01 00:00] Guard #10 begins shift', '[1518-11-01 00:05] falls asleep', '[1518-11-01 00:25] wakes up', '[1518-11-01 00:30] falls asleep', '[1518-11-01 00:55] wakes up', '[1518-11-01 23:58] Guard #99 begins shift', '[1518-11-02 00:40] falls asleep', '[1518-11-02 00:50] wakes up', '[1518-11-03 00:05] Guard #10 begins shift', '[1518-11-03 00:24] falls asleep', '[1518-11-03 00:29] wakes up', '[1518-11-04 00:02] Guard #99 begins shift', '[1518-11-04 00:36] falls asleep', '[1518-11-04 00:46] wakes up', '[1518-11-05 00:03] Guard #99 begins shift', '[1518-11-05 00:45] falls asleep', '[1518-11-05 00:55] wakes up]'])
    240
    """
    schedule = get_schedule(puzzle_input)
    guard_schedule = get_guard_schedule(schedule)
    total_minutes_asleep = []
    for guard_id, counter in guard_schedule.items():
        total_minutes_asleep.append((sum(counter.values()), guard_id))
    _, guard_id = max(total_minutes_asleep)
    minute = guard_schedule[guard_id].most_common()[0][0]
    return int(guard_id) * minute


def part_2(puzzle_input):
    """
    >>> part_2(['[1518-11-01 00:00] Guard #10 begins shift', '[1518-11-01 00:05] falls asleep', '[1518-11-01 00:25] wakes up', '[1518-11-01 00:30] falls asleep', '[1518-11-01 00:55] wakes up', '[1518-11-01 23:58] Guard #99 begins shift', '[1518-11-02 00:40] falls asleep', '[1518-11-02 00:50] wakes up', '[1518-11-03 00:05] Guard #10 begins shift', '[1518-11-03 00:24] falls asleep', '[1518-11-03 00:29] wakes up', '[1518-11-04 00:02] Guard #99 begins shift', '[1518-11-04 00:36] falls asleep', '[1518-11-04 00:46] wakes up', '[1518-11-05 00:03] Guard #99 begins shift', '[1518-11-05 00:45] falls asleep', '[1518-11-05 00:55] wakes up]'])
    4455
    """
    schedule = get_schedule(puzzle_input)
    guard_schedule = get_guard_schedule(schedule)
    most_asleep_minutes = []
    for guard_id, counter in guard_schedule.items():
        most_asleep_minutes.append((counter.most_common()[0][::-1], guard_id))
    (_, minute), guard_id = max(most_asleep_minutes)
    return int(guard_id) * minute


def main():
    puzzle_input = read_input()
    print('Answer for Part 1 is:', part_1(puzzle_input))
    print('Answer for Part 2 is:', part_2(puzzle_input))


if __name__ == '__main__':
    main()
