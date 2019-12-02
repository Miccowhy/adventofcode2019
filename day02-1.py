#!/usr/bin/python3
import operator

with open("src/02", "r") as input:
    list = input.split(",")
i = 0
operator = {1: operator.add,
2: operator.mult}
list[1] = 12
list[2] = 2

while i := i+4:
    if list[i] == 99: break
    list[list[i+3]] = operator[list[i]](list[list[i+1]], list[list[i+2])

print(list[0])
