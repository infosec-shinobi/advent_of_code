# https://adventofcode.com/2020/day/10
# --- Day 10: Adapter Array ---

def recursive_lookup(testing_adp, all_adps, ref_dict):
    if testing_adp == len(all_adps)-1:
        return 1
    if testing_adp in ref_dict:
        return ref_dict[testing_adp]

    usable_combos = 0

    for item in range(testing_adp+1, len(all_adps)):
        if all_adps[item] - all_adps[testing_adp] <= 3:
            usable_combos += recursive_lookup(item, all_adps, ref_dict)

    ref_dict[testing_adp] = usable_combos
    return usable_combos

def main():
    #open input file
    f = open("input.txt", "r")

    input_list = []

    #read each line and add to list
    for x in f:
        input_list.append(int(x.strip()))

    #exercise part 1
    #Add start and finish to list
    input_list.append(0)
    input_list.sort()
    input_list.append(input_list[-1] + 3)
    print(input_list)
    #built_in_adp = input_list[-1] + 3
    current_jolts = 0 #initial value is based on the plug jolts
    tracking_dict = {"One" : 0, "Three" : 0}

    #loop thru the list and update dict
    for item in input_list:
        if item - current_jolts == 1:
            tracking_dict["One"] =  tracking_dict.get('One', 0) + 1
        elif item - current_jolts == 3:
            tracking_dict["Three"] =  tracking_dict.get('Three', 0) + 1
        else:
            continue
        current_jolts = item

    print(f"1 jolt diffs: {tracking_dict['One']}\n3 jolt diffs: {tracking_dict['Three']}\nmultiplied together: {tracking_dict['One']*tracking_dict['Three']}")

    #exercise part 2
    master_dict = {}
    print(recursive_lookup(0, input_list, master_dict))
    
if __name__ == "__main__":
    main()