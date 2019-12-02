#!/usr/bin/python3

# Advent of Code 2019
# Day 1

fuel_count = lambda x: x // 3 - 2


def calculate_fuel_recursion(atomic_mass):
    atomic_mass = fuel_count(atomic_mass)
    return atomic_mass + calculate_fuel_recursion(atomic_mass) if atomic_mass > 0 else 0


def calculate_fuel_requirement():
    mass = [int(element) for element in open("input/01").read().splitlines()]
    module_mass_fuel = sum([fuel_count(element) for element in mass])
    whole_fuel = sum([calculate_fuel_recursion(element) for element in mass])

    return module_mass_fuel, whole_fuel


if __name__ == "__main__":
    answer = calculate_fuel_requirement()

    print(f"""
    Module fuel requirement: {answer[0]}
    Full fuel requirement: {answer[1]}
    """)

