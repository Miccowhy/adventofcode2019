#!/usr/bin/python3
# Advent of Code 2019
# Day 2

import sys
sys.path.append('../')
from intcode.intcode import Intcode

task_input = [int(element) for element in open("input").read().rstrip().split(",")]

def run1202(noun: int, verb: int):
    num = task_input.copy()
    num[1] = noun
    num[2] = verb
    task1 = Intcode(num)
    task1()
    return num[0]


def intcode_iterate(stop_value: int):
    for noun in range(100):
        for verb in range(100):
            val = 100 * noun + verb if run1202(noun, verb) == stop_value else None
            if val is not None:
                return val


if __name__ == "__main__":
    # Task 1
    print(run1202(12, 2))

    # Task 2
    print(intcode_iterate(19690720))
