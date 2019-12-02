#!/usr/bin/python3
import operator

with open("src/02", "r") as input:
    list = input.split(",")
i = 0
operator = {1: operator.add,
2: operator.mult}
while list[i:= i+4] != 99:
    list[list[i+3]] = operator[list[i]](list[list[i+1]], list[list[i+2])

print(list[0])
