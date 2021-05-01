import math

def get_fuel_a(mass):
    """get fuel req for mass for part a"""
    #divide by three, round down, and subtract 2.

    fuel_req = (math.floor(mass/3)-2)

    return fuel_req

def get_fuel_b(fuel):
    """get fuel req for fuel for part b"""
    #divide by three, round down, and subtract 2.
    temp_addit_fuel = 0
    addit_fuel_req = (math.floor(fuel/3)-2)
    
    #if 0 or negative value, no additional fuel needed
    if addit_fuel_req <=0:
        return temp_addit_fuel
    else:
        #recursively call the function until you get 0 or negative value
        temp_addit_fuel = temp_addit_fuel + addit_fuel_req
        temp_addit_fuel = temp_addit_fuel + get_fuel_b(addit_fuel_req)
        return temp_addit_fuel

def main():
    #open input file
    f = open("input.txt", "r")
    #f = open("ex_input.txt", "r")

    input_list = []
    fuel_list = []
    total_fuel_req = 0

    #read each line and add to list
    for line in f:
        mass_fuel = 0
        line = int(line.strip())
        input_list.append(line)
        mass_fuel = get_fuel_a(line)
        fuel_list.append(mass_fuel)
        total_fuel_req = total_fuel_req + mass_fuel

    #for part b, get the additional fuel req for the fuel for the fuel for the fuel....
    for req_fuel in fuel_list:
        total_fuel_req = total_fuel_req + get_fuel_b(req_fuel)

    print(f"Total fuel required: {total_fuel_req}")

if __name__ == "__main__":
    main()
