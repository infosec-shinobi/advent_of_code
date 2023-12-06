import copy

input_mappings = {}
seed_map = {}
current_text = "seed_list"
map_order = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']

def find_mapping(seed_cur_mapping, destination_start, source_start, map_range):
    if int(source_start) <= seed_cur_mapping <= int(source_start)+int(map_range):
        return(int(destination_start) + (seed_cur_mapping-int(source_start)))
    else:
        return(False)
   
#with open('ep1.txt') as f:
with open('i.txt') as f:
    count = 1
    for line in f:
        line = line.strip()
        if count == 1:
            _, seeds = line.split(": ")
            for seed in seeds.split():
                seed_map[seed] = {"start":int(seed)}
            find_text = True
        elif line == "":
            find_text = False
        elif find_text == False:
            current_text, _ = line.split()
            find_text = True
            input_mappings[current_text] = []
        else:
            temp_list = line.split()
            input_mappings[current_text].append(temp_list)
        count += 1

previous_map_name = "start"
current_map_name = ""
for mapping_name in map_order:
    current_map_name = mapping_name
    temp_map = {}
    for seed in seed_map.keys():
        temp_map[seed] = {seed_map[seed][previous_map_name]:""}
    for testing_map in input_mappings[mapping_name]:
        for seed, last_mapping in temp_map.items():
            for old_map,new_map in last_mapping.items():
                if new_map == "":
                    new_map_found = find_mapping(old_map, testing_map[0], testing_map[1], testing_map[2])
                    if new_map_found:
                        temp_map[seed][old_map] = new_map_found
    for seed, last_mapping in temp_map.items():
        for old_map,new_map in last_mapping.items():
            if new_map == "":
                seed_map[seed][mapping_name] = old_map
            else:
                seed_map[seed][mapping_name] = new_map
    previous_map_name = current_map_name

lowest_location = None
for seed,various_mappings in seed_map.items():
    if not lowest_location or lowest_location> various_mappings["humidity-to-location"]:
        lowest_location = various_mappings["humidity-to-location"]

print(f'Part 1: {lowest_location}')