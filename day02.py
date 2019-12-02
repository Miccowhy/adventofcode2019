#!/usr/bin/python3
# Advent of Code 2019
# Day 2

import operator

task_input = open("input/02").read().rstrip().split(",")
task_input = [int(element) for element in task_input]
operator = {1: operator.add,
            2: operator.mul}


def intcode(noun: int, verb: int):
    num = task_input.copy()
    num[1] = noun
    num[2] = verb
    i = 0
    while num[i] != 99 and i <= len(num):
        num[num[i+3]] = operator[num[i]](num[num[i+1]], num[num[i+2]])
        i += 4
    return num[0]


def intcode_iterate(stop_value: int):
    for noun in range(100):
        for verb in range(100):
            val = 100 * noun + verb if intcode(noun, verb) == stop_value else None
            if val is not None:
                return val


if __name__ == "__main__":
    # Task 1
    print(intcode(12, 2))

    # Task 2
    print(intcode_iterate(19690720))
