#!/usr/bin/python3
# Advent of Code 2019
# Day 3

from typing import Tuple, List

split_data = lambda x: [element.split(",") for element in x.splitlines()]

closest_manhattan_distance = lambda first, second: min(
    (abs(intersection[0]) + abs(intersection[1])
     for intersection in set(first) & set(second) if intersection != (0, 0)))

step_count = lambda first, second: min(
    (first.index(intersection) + second.index(intersection)
     for intersection in set(first) & set(second) if intersection != (0, 0)))


def path(moves: List[str]):
    directions = {"R": 1, "L": -1, "U": 1j, "D": -1j}
    wiring: List[Tuple[int, int]] = [(0, 0)]

    for move in moves:
        [wiring.append((wiring[-1][0] + int(directions[move[0]].real),
                        wiring[-1][1] + int(directions[move[0]].imag)))
         for _ in range(int(move[1:]))]

    return wiring


def unpack_paths(input_data):
    wires = [path(wire) for wire in split_data(input_data)]
    return wires[0], wires[1]


if __name__ == "__main__":
    wires = unpack_paths(open("input").read())
    print(f"Manhattan distance: {closest_manhattan_distance(wires[0], wires[1])}")
    print(f"Step count: {step_count(wires[0], wires[1])}")
