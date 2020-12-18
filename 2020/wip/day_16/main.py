# https://adventofcode.com/2020/day/16
# 

import re

def main():
    #open input file
    f = open("input.txt", "r")

    #placeholders
    input_list = []
    allowed_nums = []
    my_ticket = []
    invalid_nums = []

    #read each line and add to list
    for x in f:
        input_list.append(x.strip())

    #find index values of where sections start/end
    your_ticket_start = input_list.index("your ticket:")
    nearby_ticket_start = input_list.index("nearby tickets:")
    rules_end = input_list.index("")

    #parse file into separate sections
    my_ticket = [item.strip() for item in input_list[your_ticket_start+1].split(',')]
    temp_rules = input_list[0:rules_end]

    #get list of allowable numbers
    for rule in temp_rules:
        temp_line = re.split(': | or ',rule)
        parsed_num_range = temp_line[1:]
        for num_range in parsed_num_range:
            temp_range = num_range.split("-")
            for number in range(int(temp_range[0]),int(temp_range[1])+1):
                allowed_nums.append(number)

    #check for invalid nums in nearby tix
    temp_nearby = input_list[nearby_ticket_start+1:]
    for nearby_tix in temp_nearby:
        temp_nearby_values = nearby_tix.split(",")
        for num in temp_nearby_values:
            if int(num) not in allowed_nums:
                invalid_nums.append(int(num))

    print(f"All invalid nums: {invalid_nums}")
    print(f"Sum of all invalid nums: {sum(invalid_nums)}")

if __name__ == "__main__":
    main()