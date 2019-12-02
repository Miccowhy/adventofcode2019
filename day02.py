#!/usr/bin/python3
import operator

list = open("input/02").read().rstrip().split(",")
list = [int(element) for element in list]
i = 0
operator = {1: operator.add,
    2: operator.mul}
list[1] = 12
list[2] = 2

while list[i] != 99:
    list[list[i+3]] = operator[list[i]](list[list[i+1]], list[list[i+2]])
    i += 4
print(list[0])
