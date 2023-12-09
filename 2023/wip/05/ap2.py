import copy

input_mappings = {}
seed_map = {}
current_text = "seed_list"
map_order = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']

def find_mapping(seed_cur_range, destination_start, source_start, map_range):
    print(f"{seed_cur_range =}")
    beg_range = seed_cur_range[0]
    end_range = seed_cur_range[1]
    if int(source_start) <= beg_range:
        if end_range <= int(source_start)+int(map_range):
            return [[int(destination_start) + (beg_range-int(source_start)), int(destination_start) + (end_range-int(source_start))],[]]
        else:
            return [[int(destination_start) + (beg_range-int(source_start)), int(destination_start) + (beg_range+int(map_range))],[(beg_range+int(map_range)+1),end_range]]
    else:
        return(False)
   
with open('ep2.txt') as f:
#with open('i.txt') as f:
    count = 1
    for line in f:
        line = line.strip()
        if count == 1:
            _, seeds = line.split(": ")
            seed_list = seeds.split()
            for cur_place in range(0, len(seed_list), 2):
                temp_list = []
                temp_list.append(int(seed_list[cur_place]))
                temp_list.append(int(seed_list[cur_place])+int(seed_list[cur_place+1]))
                seed_map[cur_place] = {"start":[temp_list]}
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
print(seed_map)
print("done ingesting data")
previous_map_name = "start"
current_map_name = ""
for mapping_name in map_order:
    current_map_name = mapping_name
    temp_map = {}
    print(seed_map)
    for seed in seed_map.keys():
        temp_map[seed] = {"old":seed_map[seed][previous_map_name],"new":[]}
    print(f"{temp_map =}")
    for testing_map in input_mappings[mapping_name]:
        print(testing_map)
        for seed, mapping_data in temp_map.items():
            convert_data = mapping_data["old"]
            for seed_range in convert_data:
                new_map_found = find_mapping(seed_range, testing_map[0], testing_map[1], testing_map[2])
                print(f"{new_map_found =}")
                if new_map_found:
                    temp_map[seed]["new"].append(new_map_found[0])
                    if new_map_found[1] != []:
                        convert_data.append(new_map_found[1])
    for seed, last_mapping in temp_map.items():
        new_seed_values = []
        new_seed_values.extend(last_mapping["new"])
        new_seed_values.extend(last_mapping["old"])
        seed_map[seed][mapping_name] = new_seed_values
    previous_map_name = current_map_name
    print("boop")
print(seed_map)
#lowest_location = None
#for seed,various_mappings in seed_map.items():
#    if not lowest_location or lowest_location> various_mappings["humidity-to-location"]:
#        lowest_location = various_mappings["humidity-to-location"]

#print(f'Part 1: {lowest_location}')