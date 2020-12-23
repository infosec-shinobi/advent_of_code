# https://adventofcode.com/2020/day/21
# --- Day 21: Allergen Assessment ---

import re

def main():
    #open input file
    f = open("input.txt", "r")

    input_list = []
    allergy_dict = {}
    all_food_dict = {}
    known_allergies = []

    #read each line and add to list
    for x in f:
        temp_item = x.strip()
        temp_item = temp_item[0:-1]
        temp_line = re.split(r'\s\(contains\s', temp_item)
        ingredients = temp_line[0].split(" ")
        allergies = re.split(r',\s', temp_line[1])

        #Separate ingredients and allergies
        for ingred in ingredients:
            all_food_dict[ingred] = all_food_dict.get(ingred, 0) + 1
        
        for death_item in allergies:
            if death_item in allergy_dict:
                existing_set = set(allergy_dict[death_item])
                new_set = set(ingredients)
                temp_allergy_list = list(existing_set.intersection(new_set)) 

                if len(temp_allergy_list) == 1:
                    known_allergies.extend(temp_allergy_list)
                    allergy_dict[death_item] = temp_allergy_list
                else:
                    for index, item in enumerate(temp_allergy_list):
                        if item in known_allergies:
                            temp_allergy_list.pop(index)
                    allergy_dict[death_item] = temp_allergy_list
            else:
                allergy_dict[death_item] = ingredients
    #Make sure all allergies are in known allergy dictionary
    for key, value in allergy_dict.items():
        if len(value) == 1:
            if value[0] not in known_allergies:
                known_allergies.extend(value)
        else:
            temp_values = value
            for index, item in enumerate(value):
                if item in known_allergies:
                    temp_values.pop(index)
            
            known_allergies.extend(temp_values)
            allergy_dict[key] = temp_values

    non_allergy_ingts = 0

    #Answer to part 1
    for key, value in all_food_dict.items():
        if key not in known_allergies:
            non_allergy_ingts += int(value)
    print(f"Number of ingredients without allergies: {non_allergy_ingts}")
    
    #Answer to part 2
    #Sort allergy dictionary by keys 
    sorted_dict = sorted(allergy_dict)
    dangerous_list = []

    #Make list of ingredients with allergies
    for ingrt in sorted_dict:
        dangerous_list.extend(allergy_dict[ingrt])

    final_dedup_list = []
    #Need to dedup list
    [final_dedup_list.append(x) for x in dangerous_list if x not in final_dedup_list]

    #Translate list to string seperated by comma with no spaces
    final_string = ""
    for item in final_dedup_list:
        if final_string == "":
            final_string = item
        else:
            final_string = final_string + "," + item
    
    print(f"Final string: {final_string}")

if __name__ == "__main__":
    main()