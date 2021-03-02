# https://adventofcode.com/2020/day/23
# --- Day 23: Crab Cups ---

class Node:
    def __init__(self, value):
        self.value = value
    
    def set_next(self, next_node):
        self.next = next_node
    
    def get_next(self):
        return self.next
    
    def __repr__(self):
        return f"Cup({self.value})"

def shuffle_cups(cup_order, move_count, max_len, cur_cup, cur_cup_idx):
    """crab shuffles the cups"""

    cup_dict = {}
    prev_node = None
    first_node = None
    for idx, cup in enumerate(cup_order):
        if idx == 0:
            cup_dict[cup] = Node(cup)
        elif idx == max_len:
            cup_dict[cup] = Node(cup)
            cup_dict[cup_order[prev_node]].set_next(cup)
            cup_dict[cup].set_next(0)
        else:
            cup_dict[cup] = Node(cup)
            cup_dict[cup_order[prev_node]].set_next(cup)
        
        prev_node = idx

    for move in range(1,move_count+1):
        print("="*80)
        print(f"Move {move} occuring!")
        next_cup = cup_dict[cur_cup].get_next
        print(next_cup)
        sec_next_cup = cup_dict[next_cup].get_next
        third_next_cup = cup_dict[sec_next_cup].get_next
        fourth_next_cup = cup_dict[fourth_next_cup].get_next
        
        destination_cup = cur_cup - 1
        valid = False
        while not valid:
            if destination_cup == 0:
                    destination_cup = max_len+1
            elif destination_cup not in picked_up_cups:
                valid = True
            else: 
                destination_cup -= 1
        next_dest_cup = cup_dict[destination_cup].get_next

        cup_dict[cur_cup].set_next(fourth_next_cup)
        cur_cup=fourth_next_cup
        cup_dict[destination_cup].set_next(next_cup)
        cup_dict[third_next_cup].set_next(next_dest_cup)
    
    lookup_cup = 1
    while True:
        final_order = []
        temp_num = cup_dict[lookup_cup].get_next()
        final_order.append(temp_num)
        lookup_cup = temp_num
        if lookup_cup == 1:
            break
    print(final_order)
    #return cup_order

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
    # Need to implment Linked List because brute force is hella slow
    '''part_2_list = input_list
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
    '''
if __name__ == "__main__":
    main()