#!/usr/env julia
# Advent of Code 2019
# Day 4, task 1
doubledigit(password) = true in (password[i] == password[i+1] for i in 1:5)
ascending(password) = !(false in (password[i] <= password[i+1] for i in 1:5))

println(sum(doubledigit(string(password)) && ascending(string(password)) for password in 146810:612564))
