#Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2

def fuel(mass):
    return (mass // 3) - 2

def all_the_fuel(mass):
    dividend_fuel = fuel(mass)
    return_fuel = dividend_fuel
    while True:
        dividend_fuel = fuel(dividend_fuel)
        if dividend_fuel < 0:
            break
        return_fuel += dividend_fuel
    return return_fuel

print(all_the_fuel(14))
print(all_the_fuel(1969))
print(all_the_fuel(100756))

with open("input1-1.txt") as file:
    lines = file.readlines()

    total = 0
    
    for line in lines:
        num = int(line)
        fuel_for_mass = all_the_fuel(num)
        total += fuel_for_mass
        #print(fuel_for_mass)
    print(total)