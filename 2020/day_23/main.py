# https://adventofcode.com/2020/day/23
# --- Day 23: Crab Cups ---

def shuffle_cups(cup_order, move_count, max_len, cur_cup, cur_cup_idx):
    """crab shuffles the cups"""
    for move in range(1,move_count+1):
        print(move)
        if cur_cup_idx + 1 > max_len:
            picked_cup_idx = [0,1,2]
        elif cur_cup_idx + 2 > max_len:
            picked_cup_idx = [cur_cup_idx + 1,0,1]
        elif cur_cup_idx + 3 > max_len:
            picked_cup_idx = [cur_cup_idx + 1, cur_cup_idx + 2, 0]
        else:
            picked_cup_idx = [cur_cup_idx + 1, cur_cup_idx + 2, cur_cup_idx + 3]
        
        #print("="*80)
        #print(f"Current cup index: {cur_cup_idx} len max: {max_len} picked cup index: {picked_cup_idx}")
        #print("/"*80)
        #print(f"Move num: {move}")
        #print(f"Current Cup: {current_cup}")
        #print(f"cups: {input_list}")
        picked_up_cups = []
        
        for item in picked_cup_idx:
            picked_up_cups.append(cup_order[item])
        #print(f"PU Index: {picked_cup_idx}")
        #print(f"pick up: {picked_up_cups}")
        
        destination_cup = cur_cup - 1
        valid = False
        while not valid:
            if destination_cup == 0:
                    destination_cup = max_len+1
            elif destination_cup not in picked_up_cups:
                valid = True
            else: 
                destination_cup -= 1
        
        sorted_cup_inx = sorted(picked_cup_idx, reverse=True)
        #picked_up_cups.reverse()

        for item in sorted_cup_inx:
            cup_order.pop(item)
        
        dest_cup_idx = cup_order.index(destination_cup) + 1
        #print(f"Destination cup: {destination_cup} index: {dest_cup_idx}")

        for cup_label in range(len(picked_up_cups)):
            #print(cup_label)
            #print(cup_order)
            cup_order.insert(dest_cup_idx+cup_label,picked_up_cups[cup_label])

        #print(cup_order)

        cur_cup_idx = cup_order.index(cur_cup)

        if cur_cup_idx == max_len:
            cur_cup_idx = 0
        else:
            cur_cup_idx += 1

        cur_cup = cup_order[cur_cup_idx]
    return cup_order

def main():
    #open input file
    f = open("input.txt", "r")

    input_list = []
    original_list = []

    #read each line and add to list
    for x in f:
        temp_str = x.strip()
        for num in temp_str:
            input_list.append(int(num))

    # PART 1
    part_1_list = input_list
    part_1_moves = 100
    part_1_max_len = len(part_1_list) - 1
    print(f"p1 length is {part_1_max_len}")
    print(f"Last num is: {part_1_list[part_1_max_len]}")
    p1_current_cup_index = 0  
    p1_current_cup = part_1_list[p1_current_cup_index]
    part_1_list = shuffle_cups(part_1_list, part_1_moves, part_1_max_len,p1_current_cup, p1_current_cup_index)

    p1_final_list = []
    p1_cup_one_idx = part_1_list.index(1)
    if p1_cup_one_idx == part_1_max_len:
        p1_final_list = part_1_list[0:len(part_1_list)]
    elif p1_cup_one_idx == 0:
        p1_final_list = part_1_list[1:]
    else:
        p1_final_list = part_1_list[p1_cup_one_idx+1:len(part_1_list)]
        p1_final_list.extend(part_1_list[0:p1_cup_one_idx])
   
    p1_final_string = ""
    for num in p1_final_list:
        p1_final_string = p1_final_string+str(num)
    print(p1_final_string)

    # PART 2
    part_2_list = input_list
    part_2_moves = 10000000
    for x in range(10,1000001):
        part_2_list.append(int(x))
    part_2_max_len = len(part_2_list) - 1
    print(f"p2 length is {part_2_max_len}")
    print(f"Last num is: {part_2_list[part_2_max_len]}")
    p2_current_cup_index = 0
    p2_current_cup = part_2_list[p2_current_cup_index]
    part_2_list = shuffle_cups(part_2_list, part_2_moves, part_2_max_len, p2_current_cup, p2_current_cup_index)
   
    p2_cup_one_idx = part_2_list.index(1)
    neighbor_1 = part_2_list[p2_cup_one_idx+1]
    neighbor_2 = part_2_list[p2_cup_one_idx+2]
    print(f"N1 is {neighbor_1}, N2 is {neighbor_2}, product of them is: {neighbor_1*neighbor_2}")
    
if __name__ == "__main__":
    main()