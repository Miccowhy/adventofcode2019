#!/usr/bin/python3
# Advent of Code 2019
# Day 5

import operator
from collections import deque

task_input = open("input").read().rstrip().split(",")
task_input = [int(element) for element in task_input]


def write_input(value, *_):
    data[value] = "5"  # 1: 1, 2: 5


def output_parameter(value, *_):
    print(data[value])


instruction = {1: operator.add,
               2: operator.mul,
               3: write_input,
               4: output_parameter}


def opcode_expansion(value):
    opcode = deque(str(value))
    if len(opcode) < 5:
        for i in range(len(opcode), 5):
            opcode.appendleft('0')
    return opcode


def intcode(data):
    i = 0
    while data[i] != 99 and i < len(data):
        opcode = opcode_expansion(data[i])
        c, b, a = [int(i + 3 - digit) if int(opcode[digit]) else int(data[i + 3 - digit]) for digit in range(3)]

        if opcode[-1] == '1':
            data[c] = instruction[1](data[a], data[b])
            if c != i:
                i += 4
        elif opcode[-1] == '2':
            data[c] = instruction[2](data[a], data[b])
            if c != i:
                i += 4
        elif opcode[-1] == '3':
            instruction[3](a)
            if a != i:
                i += 2
        elif opcode[-1] == '4':
            output_parameter(a)
            i += 2

        elif opcode[-1] == '5':
            if data[a]:
                data[i] = data[b]
            else:
                i += 3
        elif opcode[-1] == '6':
            if not data[a]:
                data[i] = data[b]
            else:
                i += 3
        elif opcode[-1] == '7':
            data[c] = 1 if data[a] < data[b] else 0
            if c != i:
                i += 4
        elif opcode[-1] == '8':
            data[c] = 1 if data[a] == data[b] else 0
            if c != i:
                i += 4

        else:
            print(f"fuck: {i}")
            break


if __name__ == "__main__":
    global data
    data = task_input.copy()

    intcode(data)
