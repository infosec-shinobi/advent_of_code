# https://adventofcode.com/2020/day/13
# --- Day 13: Shuttle Search ---

from math import ceil

def find_closest_bus(depart_time, bus_list):
    """find the bus that is closest to the depart time"""

    master_dict = {}
    for bus in bus_list:
        if bus == "x":
            continue
        else:
            current_bus = int(bus)
            #Divide bus time by bus id and round up to find the 
            # number of trips the bus needs to make to reach at 
            # least the depart time
            trips_till_depart = ceil(depart_time/current_bus)
            master_dict[bus] = current_bus * trips_till_depart

    return master_dict

def main():
    #open input file
    f = open("input.txt", "r")

    input_list = []

    #read each line and add to list
    for x in f:
        input_list.append(x)

    for index in range(len(input_list)):
        #get the depart time
        if index == 0:
            temp_str = input_list[index]
            temp_str = temp_str.strip()
            input_list[index] = int(temp_str)
        #get the possible buses
        else:
            temp_str = input_list[index]
            temp_list = temp_str.split(",")
            input_list[index] = temp_list

    #find all the bus times closest to the depart time
    bus_times = find_closest_bus(input_list[0], input_list[1])

    closest_bus = 0
    closest_time = 0

    #figure out which bus has the closest depart time to what you want
    for bus,time in bus_times.items():
        if closest_time == 0:
            closest_bus = bus
            closest_time = time
        elif time - input_list[0] < closest_time - input_list[0]:
            closest_bus = bus
            closest_time = time
        else:
            continue
    time_dif = closest_time - input_list[0]
    print(f"Bus {closest_bus} departs at {closest_time} and the id*wait time is {int(closest_bus)*time_dif}")

if __name__ == "__main__":
    main()