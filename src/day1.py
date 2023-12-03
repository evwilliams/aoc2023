#!/usr/bin/env python
# coding: utf-8
import re

from parsing import line_splitter
from parsing import parse
from parsing import str_reverse


def run_on_match(line, pattern, func):
    match = re.search(pattern, line)
    return func(match[0])


def part1_parser(line):
    first = run_on_match(line, r"\d", lambda m: m)
    last = run_on_match(str_reverse(line), r"\d", lambda m: m)
    return int(first + last)


def create_part2_parser():
    mapping = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0",
    }

    keys_pattern = "|".join(mapping.keys())
    forward_pattern = re.compile(r"\d|" + keys_pattern)
    reverse_pattern = re.compile(r"\d|" + str_reverse(keys_pattern))

    def lookup_or_matched_value(m):
        return mapping[m] if m in mapping else m

    def reverse_lookup(m):
        m = str_reverse(m)
        return lookup_or_matched_value(m)

    def inner_loop(line):
        first = run_on_match(line, forward_pattern, lookup_or_matched_value)
        last = run_on_match(str_reverse(line), reverse_pattern, reverse_lookup)
        return int(first + last)

    return inner_loop


def solve(filename, parser):
    result = parse(
        filename=filename,
        splitter=line_splitter,
        filterer=lambda s: len(s) > 0,
        parser=parser,
    )
    return sum(result)


print(f'Result: {solve("day1.txt", part1_parser)}')
print(f'Result: {solve("day1.txt", create_part2_parser())}')
