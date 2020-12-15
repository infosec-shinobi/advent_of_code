# https://adventofcode.com/2020/day/14
# --- Day 14: Docking Data ---
import re

def perform_bitwise_op(mask, num_to_mask):
    """Apply mask to number"""
    raw_list = []
    mask_list = []
    new_list = []
    return_string = ""

    for char in num_to_mask:
        raw_list.append(char)
    for char in mask:
        mask_list.append(char)

    for index, item in enumerate(num_to_mask):
        mask_value = mask_list[index]
        if mask_value == "X":
            new_list.append(item)
        elif item == mask_value:
            new_list.append(item)
        else:
            new_list.append(mask_value)

    return return_string.join(new_list)

def main():
    #open input file
    f = open("input.txt", "r")

    input_list = []

    #read each line and add to list
    for x in f:
        temp_list = [item.strip() for item in x.split('=')]
        input_list.append(temp_list)

    print(input_list)
    current_mask = ""
    digit = re.compile('\d+') 
    master_dict = {}

    for item in input_list:
        if item[0] == "mask":
            current_mask = item[1]
            print(current_mask)
        else:
            memory = int(digit.findall(item[0])[0])
            current_mem_value = int(item[1])
            #print(current_mem_value)
            new_value = perform_bitwise_op(current_mask, f'{current_mem_value:036b}')
            #print(f'{current_mem_value:036b}')
            #print(current_mask)
            #print(new_value)
            new_mem_value = int(new_value, 2)
            master_dict[memory] = new_mem_value

    total_sum = 0

    for key, value in master_dict.items():
        total_sum += value

    print(master_dict)
    print(total_sum)

if __name__ == "__main__":
    main()