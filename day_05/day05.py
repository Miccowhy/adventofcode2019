#!/usr/bin/python3
# Advent of Code 2019
# Day 5

from collections import deque

task_input = open("input").read().rstrip().split(",")
task_input = [int(element) for element in task_input]


def intcode(data, *args):
    arguments = deque(args)
    i = 0
    while data[i] != 99 and i < len(data):
        try:
            a, b, c = [i + x if data[i] // 10**(x+1) % 10 else data[i + x] for x in range(1, 4)]
        except IndexError:
            pass

        opcode = data[i] % 100
        if opcode == 99: break
        elif opcode == 1: data[c] = data[a] + data[b]; i += 4
        elif opcode == 2: data[c] = data[a] * data[b]; i += 4
        elif opcode == 3: data[a] = arguments.popleft(); i += 2  #
        elif opcode == 4: print(data[a]); i += 2
        elif opcode == 5: i = data[b] if data[a] else i + 3
        elif opcode == 6: i = data[b] if not data[a] else i + 3
        elif opcode == 7: data[c] = 1 if data[a] < data[b] else 0; i = i + 4
        elif opcode == 8: data[c] = 1 if data[a] == data[b] else 0; i = i + 4


if __name__ == "__main__":
    intcode(task_input.copy(), 1)  # Task 1

    intcode(task_input.copy(), 5)  # Task 2
