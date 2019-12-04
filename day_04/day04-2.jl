#!/usr/env julia
# Advent of Code 2019
# Day 4, task 2
# Very naive solution
ascending(password) = !(false in (password[i] <= password[i+1] for i in 1:5))

function naive_doubles(password)
        seq = [0]
        let i = 1, j = 1
                while i <= 6 && j <= 6
                        if password[i] == password[j]
                                seq[end] += 1
                                j += 1
                        else
                                append!(seq, 0)
                                i = j
                        end
                end
        end
        2 in seq
end

println(sum(naive_doubles(string(password)) && ascending(string(password)) for password in 146810:612564))
