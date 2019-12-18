#!/usr/bin/python3
# Advent of Code 2019
# Day 7

import sys
sys.path.append('../')
from itertools import permutations
from intcode.intcode import Intcode

data = [int(element) for element in open("input", "r").read().rstrip().split(",")]

def amplifier_wrapper(amp_data, sequence, signal=0):
    for phase in sequence:
        ic = Intcode(amp_data, phase, signal)
        ic()
        signal = ic.output
    return signal

if __name__ == "__main__":
    print(
        max(amplifier_wrapper(data.copy(), sequence)
            for sequence in permutations([0, 1, 2, 3, 4])))

