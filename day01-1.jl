#!/usr/env julia
data = parse.(Int,readlines("input/01"))
fuel_count(mass) = mass ÷ 3 - 2

println(sum(fuel_count.(data)))
