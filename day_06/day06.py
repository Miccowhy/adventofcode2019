#!/usr/bin/python3
# Advent of Code 2019
# Day 6

orbits = dict()
data = open("input").read()


def compute_orbits(center):
    return 1 + compute_orbits(orbits[center]) if center in orbits else 0


def set_orbits(data):
    for line in data.splitlines():
        line = line.split(")")
        orbits[line[1]] = line[0]


def sum_all_orbits():  # Task 1
    return sum(compute_orbits(center) for center in orbits)


def path_to_root(node, path=None):
    if path is None:
        path = list()
    if node in orbits:
        path.append(node)
        path_to_root(orbits[node], path)
    return path


def compute_distance_between():  # Task 2
    first_path = path_to_root(orbits["YOU"])
    second_path = path_to_root(orbits["SAN"])

    for i in range(len(first_path)):
        if first_path[i] in set(second_path):
            return i + second_path.index(first_path[i])


if __name__ == "__main__":
    set_orbits(data)

    print(sum_all_orbits())
    print(compute_distance_between())
