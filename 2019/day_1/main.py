import math

def get_fuel_a(mass):
    """get fuel req for mass for part a"""
    #divide by three, round down, and subtract 2.

    fuel_req = (math.floor(mass/3)-2)
    print(f"Input is: {mass} and fuel req is: {fuel_req}")
    return fuel_req


def main():
    #open input file
    f = open("input.txt", "r")
    #f = open("ex_input.txt", "r")

    input_list = []
    total_fuel_req = 0

    #read each line and add to list
    for line in f:
        line = int(line.strip())
        input_list.append(line)
        total_fuel_req = total_fuel_req + get_fuel_a(line)

    print(input_list)
    print(total_fuel_req)

if __name__ == "__main__":
    main()
