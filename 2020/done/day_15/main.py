# https://adventofcode.com/2020/day/15
# --- Day 15: Rambunctious Recitation ---

def main():
    #open input file
    f = open("input.txt", "r")

    input_list = []

    #read each line and add to list
    for x in f:
        temp_list = [item.strip() for item in x.split(',')]
        input_list.append(temp_list)

    #Tracker vars
    count = 1
    age_dict = {}
    desired_turn = 2020
    #desired_turn = 30000000
    last_num = 0
    heard_before = False
    temp_num_list = [0,0]

    #Cycle through input for first turns
    for item in input_list:
        for num in item:
            #if we have heard the number before, update the dict
            if num in age_dict:
                heard_before = True
                temp_num_list = age_dict[int(num)]
                temp_num_list = [temp_num_list[1], count]
            else:
                temp_num_list = [0,count]
            age_dict[int(num)] = temp_num_list
            count += 1
            last_num = num
    #while we have not done all the turns
    while count <= desired_turn:
        #if the number hasn't been seen, say 0 and  update dict
        if not heard_before:
            new_num = 0
            if 0 in age_dict:
                temp_num_list = age_dict[0]
                temp_num_list = [temp_num_list[1], count]
                age_dict[0] = temp_num_list
                heard_before = True
            else:
                temp_num_list = [0,count]
                age_dict[0] = temp_num_list
            count += 1
            last_num = 0
        else:
            heard_before = False
            temp_num_list = age_dict[last_num]
            last_num = int(temp_num_list[1]) - int(temp_num_list[0])
            if last_num in age_dict:
                heard_before = True
                temp_num_list = age_dict[last_num]
                temp_num_list = [temp_num_list[1], count]
                age_dict[last_num] = temp_num_list
            else:
                temp_num_list = [0,count]
                age_dict[last_num] = temp_num_list
            count += 1

    print(f"Last number spoken at desired turn of {desired_turn} was {last_num}")

if __name__ == "__main__":
    main()