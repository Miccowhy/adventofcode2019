#!/usr/env julia
# Advent of Code 2019
# Day 1

data = split.(readlines("input/02"),",")
num = collect(Iterators.flatten([parse.(Int, element) for element in data]))


print(num[1])