import math

fuel_count = lambda x: math.floor(x / 3) - 2


def calculate_fuel_recursion(atomic_mass):
    atomic_mass = fuel_count(atomic_mass)
    return atomic_mass + calculate_fuel_recursion(atomic_mass) if atomic_mass > 0 else 0


def calculate_fuel_requirement():
    module_mass_fuel = 0
    whole_fuel = 0
    with open("src/01", "r") as file_in:
        for mass in file_in:
            module_mass_fuel += fuel_count(int(mass))
            whole_fuel += calculate_fuel_recursion(int(mass))

    return module_mass_fuel, whole_fuel


if __name__ == "__main__":
    answer = calculate_fuel_requirement()

    print(f"""
    Module fuel requirement: {answer[0]}
    Full fuel requirement: {answer[1]} 
    """)
