#!/usr/bin/python3
# Advent of Code 2019
# Day 3

from typing import Set, Tuple, List

split_data = lambda x: [element.split(",") for element in x.splitlines()]


def path(moves: List[str]):
    last_position = (0, 0)
    wiring: Set[Tuple[int, int]] = set()

    for move in moves:
        if move[0] == "R":                                                                          # RIGHT
            [wiring.add((x, last_position[1])) for x in range(
                last_position[0], last_position[0] + int(move[1:]))]
            last_position = (last_position[0] + int(move[1:]), last_position[1])
        elif move[0] == "L":                                                                        # LEFT
            [wiring.add((x, last_position[1])) for x in range(
                last_position[0], last_position[0] - int(move[1:]), -1)]
            last_position = (last_position[0] - int(move[1:]), last_position[1])
        elif move[0] == "U":                                                                        # UP
            [wiring.add((last_position[0], y)) for y in range(
                last_position[1], last_position[1] + int(move[1:]))]
            last_position = (last_position[0], last_position[1] + int(move[1:]))
        elif move[0] == "D":                                                                        # DOWN
            [wiring.add((last_position[0], y)) for y in range(
                last_position[1], last_position[1] - int(move[1:]), -1)]
            last_position = (last_position[0], last_position[1] - int(move[1:]))

    return wiring


def find_cross(first: Set[Tuple[int, int]], second: Set[Tuple[int, int]]):
    crossed_wires = first & second
    print(crossed_wires)
    return min([abs(distance[0]) + abs(distance[1]) for distance in crossed_wires if distance != (0, 0)])


def compare(input_data):
    wires = [path(wire) for wire in split_data(input_data)]
    return find_cross(wires[0], wires[1])


if __name__ == "__main__":
    print(compare(open("input").read()))