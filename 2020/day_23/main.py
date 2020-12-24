# https://adventofcode.com/2020/day/23
# --- Day 23: Crab Cups ---

def main():
    #open input file
    f = open("input.txt", "r")

    input_list = []

    #read each line and add to list
    for x in f:
        temp_str = x.strip()
        for num in temp_str:
            input_list.append(int(num))

    num_of_moves = 100
    list_max = len(input_list) - 1
    current_cup_index = 0
    current_cup = input_list[current_cup_index]

    for move in range(1,num_of_moves+1):
        
        if current_cup_index + 1 > list_max:
            picked_cup_idx = [0,1,2]
        elif current_cup_index + 2 > list_max:
            picked_cup_idx = [current_cup_index + 1,0,1]
        elif current_cup_index + 3 > list_max:
            picked_cup_idx = [current_cup_index + 1, current_cup_index + 2, 0]
        else:
            picked_cup_idx = [current_cup_index + 1, current_cup_index + 2, current_cup_index + 3]
        
        #print("="*80)
        #print(f"Current cup index: {current_cup_index} len max: {list_max} picked cup index: {picked_cup_idx}")
        print("/"*80)
        print(f"Move num: {move}")
        print(f"Current Cup: {current_cup}")
        print(f"cups: {input_list}")
        picked_up_cups = []
        
        for item in picked_cup_idx:
            picked_up_cups.append(input_list[item])
        #print(f"PU Index: {picked_cup_idx}")
        print(f"pick up: {picked_up_cups}")
        
        destination_cup = current_cup - 1
        valid = False
        while not valid:
            if destination_cup == 0:
                    destination_cup = 9
            elif destination_cup not in picked_up_cups:
                valid = True
            else: 
                destination_cup -= 1
        
        sorted_cup_inx = sorted(picked_cup_idx, reverse=True)
        #picked_up_cups.reverse()

        for item in sorted_cup_inx:
            input_list.pop(item)
        
        dest_cup_idx = input_list.index(destination_cup) + 1
        print(f"Destination cup: {destination_cup} index: {dest_cup_idx}")

        for cup_label in range(len(picked_up_cups)):
            #print(cup_label)
            #print(input_list)
            input_list.insert(dest_cup_idx+cup_label,picked_up_cups[cup_label])

        #print(input_list)

        current_cup_index = input_list.index(current_cup)

        if current_cup_index == list_max:
            current_cup_index = 0
        else:
            current_cup_index += 1
        current_cup = input_list[current_cup_index]

    print(f"Final order: {input_list}")

    cup_one_idx = input_list.index(1)
    if cup_one_idx == list_max:
        final_list = input_list[0:len(input_list)]
    elif cup_one_idx == 0:
        final_list = input_list[1:]
    else:
        final_list = input_list[cup_one_idx+1:len(input_list)]
        print(final_list)
        final_list.extend(input_list[0:cup_one_idx])
        print(final_list)
    
    final_string = ""
    for num in final_list:
        final_string = final_string+str(num)
    print(final_string)
if __name__ == "__main__":
    main()