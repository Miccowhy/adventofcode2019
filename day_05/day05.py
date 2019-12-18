#!/usr/bin/python3
# Advent of Code 2019
# Day 5

import sys
sys.path.append('../')
from intcode.intcode import Intcode

task_input = [int(element) for element in open("input").read().rstrip().split(",")]


if __name__ == "__main__":
    task1 = Intcode(task_input.copy(), 1)
    task1()
    print(task1.output)

    task2 = Intcode(task_input.copy(), 5)
    task2()
    print(task2.output)
