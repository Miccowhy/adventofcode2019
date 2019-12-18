#!/usr/bin/python3
# Advent of Code 2019
# INTCODE Module

from collections import deque

class Intcode:

    def __init__(self, data, *args, visual=False):
        self.data = data
        self.arguments = deque(args)

        self.output: int

    def __call__(self):
        i = 0
        while True:
            try:
                a, b, c = [i + x if self.data[i] // 10**(x+1) % 10 else self.data[i + x] for x in range(1, 4)]
            except IndexError:
                pass

            opcode = self.data[i] % 100
            if opcode == 99: break
            elif opcode == 1: self.data[c] = self.data[a] + self.data[b]; i += 4
            elif opcode == 2: self.data[c] = self.data[a] * self.data[b]; i += 4
            elif opcode == 3: self.data[a] = self.arguments.popleft(); i += 2
            elif opcode == 4: self.output = self.data[a]; i += 2
            elif opcode == 5: i = self.data[b] if self.data[a] else i + 3
            elif opcode == 6: i = self.data[b] if not self.data[a] else i + 3
            elif opcode == 7: self.data[c] = 1 if self.data[a] < self.data[b] else 0; i = i + 4
            elif opcode == 8: self.data[c] = 1 if self.data[a] == self.data[b] else 0; i = i + 4

