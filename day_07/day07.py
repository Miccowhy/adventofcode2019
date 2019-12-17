#!/usr/bin/python3
# Advent of Code 2019
# Day 7

from collections import deque
from itertools import permutations

task_input = open("input").read().rstrip().split(",")
task_input = [int(element) for element in task_input]


def intcode(data, *args):
    arguments = deque(args)
    i = 0
    while i < len(data):
        try:
            a, b, c = [i + x if data[i] // 10**(x+1) % 10 else data[i + x] for x in range(1, 4)]
        except IndexError:
            pass

        opcode = data[i] % 100
        if opcode == 99: break
        elif opcode == 1: data[c] = data[a] + data[b]; i += 4
        elif opcode == 2: data[c] = data[a] * data[b]; i += 4
        elif opcode == 3: data[a] = arguments.popleft(); i += 2
        elif opcode == 4: output = data[a]; i += 2
        elif opcode == 5: i = data[b] if data[a] else i + 3
        elif opcode == 6: i = data[b] if not data[a] else i + 3
        elif opcode == 7: data[c] = 1 if data[a] < data[b] else 0; i = i + 4
        elif opcode == 8: data[c] = 1 if data[a] == data[b] else 0; i = i + 4

def amplifier_wrapper(amp_data, sequence, signal=0):
    for phase in sequence:
        signal = intcode(amp_data, phase, signal)
    return signal

if __name__ == "__main__":
    print(
        max(amplifier_wrapper(task_input.copy(), sequence)
            for sequence in permutations([0, 1, 2, 3, 4])))

