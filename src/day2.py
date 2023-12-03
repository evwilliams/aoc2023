#!/usr/bin/env python
# coding: utf-8
import math

from parsing import parse


def parse_game(line):
    splits = line.strip().split(":")
    game = int(splits[0].split(" ")[1])
    pulls = splits[1].strip().split(";")
    return game, parse_pulls(pulls)


def parse_pulls(pulls):
    all_counts = []
    for pull in pulls:
        colors = pull.strip().split(",")

        counts = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        for color in colors:
            info = color.strip().split(" ")
            num = info[0]
            clr = info[1]
            counts[clr] += int(num)

        all_counts.append(counts)
    return all_counts


def part1(filename):
    parsed = parse(
        filename=filename,
        parser=parse_game,
    )

    def impossible(actual_counts):
        constraint = {
            "red": 12,
            "green": 13,
            "blue": 14,
        }
        for key, value in constraint.items():
            constraint[key] = value - (
                actual_counts[key] if key in actual_counts else 0
            )
            if constraint[key] < 0:
                return True
        return False

    def process_parsed(parsed_game):
        game, parsed_pulls = parsed_game
        return 0 if any(map(impossible, parsed_pulls)) else game

    return sum(map(process_parsed, parsed))


def part2(filename):
    parsed = parse(
        filename=filename,
        parser=parse_game,
    )

    def process_parsed(parsed_game):
        game, parsed_pulls = parsed_game
        min_needed = {}
        for pull in parsed_pulls:
            for key, value in pull.items():
                if key not in min_needed:
                    min_needed[key] = value
                else:
                    min_needed[key] = max(value, min_needed[key])
        return math.prod(min_needed.values())

    return sum(map(process_parsed, parsed))


print(f"Result: {part1('day2.txt')}")
print(f"Result: {part2('day2.txt')}")
