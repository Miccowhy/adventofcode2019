#!/usr/bin/python3
# Advent of Code 2019
# Day 3

from typing import Set, Tuple, List

split_data = lambda x: [element.split(",") for element in x.splitlines()]

closest_manhattan_distance = lambda first, second: min(
    [abs(intersection[0]) + abs(intersection[1]) for intersection in set(first) & set(second) if intersection != (0, 0)])

step_count = lambda first, second: min(
    [first.index(intersection) + second.index(intersection) for intersection in set(first) & set(second) if intersection != (0, 0)])


def path(moves: List[str]):
    wiring: List[Tuple[int, int]] = [(0, 0)]

    for move in moves:
        previous = wiring[-1]
        if move[0] == "R":                                                                          # RIGHT
            [wiring.append((previous[0] + x, wiring[-1][1])) for x in range(1, int(move[1:]) + 1)]
        elif move[0] == "L":                                                                        # LEFT
            [wiring.append((previous[0] - x, previous[1])) for x in range(1, int(move[1:]) + 1)]
        elif move[0] == "U":                                                                        # UP
            [wiring.append((previous[0], previous[1] + y)) for y in range(1, int(move[1:]) + 1)]
        elif move[0] == "D":                                                                        # DOWN
            [wiring.append((previous[0], previous[1] - y)) for y in range(1, int(move[1:]) + 1)]

    return wiring


def unpack_paths(input_data):
    wires = [path(wire) for wire in split_data(input_data)]
    return wires[0], wires[1]


if __name__ == "__main__":
    wires = unpack_paths(open("input").read())
    print(f"Manhattan distance: {closest_manhattan_distance(wires[0], wires[1])}")
    print(f"Step count: {step_count(wires[0], wires[1])}")


