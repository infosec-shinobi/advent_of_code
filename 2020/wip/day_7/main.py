# https://adventofcode.com/2020/day/7
# --- Day 7: Handy Haversacks ---

import re

def search_dict_for_value(dict_input, values_to_find):
    """find keys that contian the desired value"""
    new_bags_to_search = []

    for key, value in dict_input.items():
        for item in values_to_find:
            if item in value:
                new_bags_to_search.append(key)

    return new_bags_to_search

def main():
    #open input file
    f = open("input.txt", "r")

    input_map = {}
    bags_to_search = []
    counted_bags = []

    #read each line, preprocess, and add to list
    for x in f:
        temp_line = re.split(' bags contain \d | bags contain no other bags.| bag[s]?, \d | bag[s]?.[\n]?|\n', x, flags=re.IGNORECASE)
        temp_line = list(filter(None, temp_line))
        input_map[temp_line[0]] = temp_line[1:]
        #print(input_map[temp_line[0]])
        if "shiny gold" in input_map[temp_line[0]]:
            bags_to_search.append(temp_line[0])


    # exercise part 1
    found = False
    while not found:
        
        if len(bags_to_search) == 0:
            shiny_gold_bags = set(counted_bags)
            final_gold_bag_possibilities = (list(shiny_gold_bags)) 
            print(f"Bag colors that can contain shiny gold bags: {len(final_gold_bag_possibilities)}")
            found = True
        else:
            counted_bags.extend(bags_to_search)
            bags_to_search = search_dict_for_value(input_map, bags_to_search)

if __name__ == "__main__":
    main()