#!/usr/bin/python3
# Advent of Code 2019
# INTCODE Module

from collections import deque

class Intcode:
    self.output: int

    def __init__(self, data, *args, default_input=True, visual=False):
        self.data = [int(element) for element in open(data.read().rstrip().split(",")] if parse else data
        self.arguments = deque(args)

        self.output = lambda value: print(value) if visual else value

    def __call__(self):
        i = 0
        while i < len(data):
            try:
                p = [i + x if self.data[i] // 10**(x+1) % 10\
                        else self.data[i + x] for x in range(1, 4)]
            except IndexError:
                pass
            opcode = self.data[i] % 100

            def operation(p):
                try:
                    p = [self.data[element] for element in p]
                if opcode == 99:
                    break
                elif opcode == 1: p[2] = p[0] + p[1]; i += 4
                elif opcode == 2: p[2] = p[0] * p[1]; i += 4
                elif opcode == 3: p[0] = self.arguments.popleft(); i += 2
                elif opcode == 4: output(p[0]); i += 2
                elif opcode == 5: i = p[1] if p[0] else i + 3
                elif opcode == 6: i = p[1] if not p[0] else i + 3
                elif opcode == 7: p[2] = 1 if p[0] < p[1] else 0; i = i + 4
                elif opcode == 8: p[2] = 1 if p[0] == p[1] else 0; i = i + 4

            operation()

    def last_output(self):
        return self.output

