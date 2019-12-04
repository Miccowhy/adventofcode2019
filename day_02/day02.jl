#!/usr/env julia
# Advent of Code 2019
# Day 2

task_input = split.(readlines("input"),",")
data = collect(Iterators.flatten([parse.(Int, element) for element in task_input]))

operator = Dict(1 => +,
                2 => *)


function intcode!(noun, verb)
    num = deepcopy(data)
    num[2] = noun
    num[3] = verb

    let i = 1
        while num[i] ≠ 99 && i ≤ length(num)
            num[num[i+3]+1] = operator[num[i]](num[num[i+1]+1], num[num[i+2]+1])
            i += 4
        end
    end
    return num[1]
end

function intcode_iterate(stop_value)
    for i = 1:100*100
        noun, verb = divrem(i-1, 100) .+ (1,1)
        if intcode!(noun, verb) == stop_value
            return 100 * noun + verb
        end
    end
end

println(intcode!(12, 2)) # Task 1
println(intcode_iterate(19690720)) # Task 2
