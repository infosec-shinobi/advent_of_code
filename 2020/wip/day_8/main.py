# https://adventofcode.com/2020/day/8
# --- Day 8: Handheld Halting ---

def list_lookup(lookup_list, index_num):
    """find the data in a list when provided the index"""
    temp_line = lookup_list[index_num]
    hit_already = temp_line[1]
    data_map = temp_line[0]

    return hit_already, data_map

def string_split(str_to_split):
    """Separate the first char from the string"""
    temp_list = []
    temp_list.append(str_to_split[0])
    temp_list.append(str_to_split[1:])

    return temp_list

def main():
    #open input file
    f = open("input.txt", "r")

    input_list = []
    
    #read each line, parse data, and add to list
    for x in f:
        temp_map = {}
        temp_list = []
        temp_split = []

        x = x.strip()
        temp_split = x.split(" ")
        temp_map[temp_split[0]] = temp_split[1]
        temp_list = [temp_map, False]
        input_list.append(temp_list)

    #exercise part 1
    accumulator = 0
    index_to_check = 0
    found = False
    
    while not found:
        seen_before = False
        index_data = {}
        temp_list = []

        #Lookup data
        seen_before, index_data = list_lookup(input_list, index_to_check)

        #process returned data
        if not seen_before:
            #Mark the index item as seen before
            input_list[index_to_check][1] = True

            #Take action depending on what the index data is
            for key in index_data:
                current_key = key
                current_value = index_data[key]
                temp_list =  string_split(current_value)
            if current_key == "acc":
                if temp_list[0] == "+":
                    accumulator += int(temp_list[1])
                else:
                    accumulator -= int(temp_list[1])
                index_to_check += 1
            elif current_key == "jmp":
                if temp_list[0] == "+":
                    index_to_check += int(temp_list[1])
                else:
                    index_to_check -= int(temp_list[1])
            elif current_key == "nop":
                index_to_check += 1
            else:
                pass
        else:
            found = True
    
    print(f"Accumulator before infinite loop begins: {accumulator}")

if __name__ == "__main__":
    main()