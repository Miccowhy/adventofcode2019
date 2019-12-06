#!/usr/bin/python3
# Advent of Code 2019
# Day 6

orbits = dict()
data = open("input").read()


def compute_orbits(center):
    if center in orbits:
        for planet in orbits[center]:
            return 1 + compute_orbits(planet)
    else:
        return 0


def set_orbits(data):
    for line in data.splitlines():
        line = line.split(")")
        if line[1] not in orbits:
            orbits[line[1]] = {line[0]}
        else:
            orbits[line[1]].add(line[0])


def task1_run():
    return sum(compute_orbits(center) for center in orbits)


# TODO: fix path returning None
def path_to_root(node, path):
    path.append(node)
    print(path)
    if node in orbits:
        [path_to_root(next_node, path) for next_node in orbits[node]]
    else:  # node == "COM":
        return path


if __name__ == "__main__":
    set_orbits(data)
    print('COM' in orbits)
    print('B' in orbits)
    for key in orbits:
        print(key)
    #print(task1_run())
    #print(path_to_root("YOU"))
    print(path_to_root("C", []))
