#!/usr/env julia
# Advent of Code 2019
# Day 1

data = parse.(Int,readlines("input"))
fuel_count(mass) = mass ÷ 3 - 2
recursive_fuel(mass) = mass > 0 ? mass + recursive_fuel(fuel_count(mass)) : 0

println("Module fuel requirement: $(sum(fuel_count.(data)))")
println("Full fuel requirement: $(sum(recursive_fuel.(fuel_count.(data))))")
