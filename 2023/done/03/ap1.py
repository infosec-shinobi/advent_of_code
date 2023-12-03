input_list = []
#with open('ep1.txt') as f:
with open('i.txt') as f:
    for line in f:
        line = line.strip()
        input_list.append(line)

max_row = len(input_list) - 1
part_nums = []
for row_num, line in enumerate(input_list):
    max_col = len(line) -1
    symb_adj = False
    temp_num = ""
    for place, item in enumerate(line):
        if item.isnumeric():
            temp_num = temp_num + str(item)
            if not symb_adj:
                #check east
                if place != 0:
                    if not line[place-1].isnumeric() and line[place-1] != ".":
                        symb_adj = True
                #check west
                if place != max_col:
                    if not line[place+1].isnumeric() and line[place+1] != ".":
                        symb_adj = True
                #check north
                if row_num != 0:
                    if not input_list[row_num-1][place].isnumeric() and input_list[row_num-1][place] != ".":
                        symb_adj = True
                #check south
                if row_num != max_row:
                    if not input_list[row_num+1][place].isnumeric() and input_list[row_num+1][place] != ".":
                        symb_adj = True
                #check north east
                if row_num != 0 and place != 0:
                    if not input_list[row_num-1][place-1].isnumeric() and input_list[row_num-1][place-1] != ".":
                        symb_adj = True
                #check north west
                if row_num != 0 and place != max_col:
                    if not input_list[row_num-1][place+1].isnumeric() and input_list[row_num-1][place+1] != ".":
                        symb_adj = True
                #check south east
                if row_num != max_row and place != 0:
                    if not input_list[row_num+1][place-1].isnumeric() and input_list[row_num+1][place-1] != ".":
                        symb_adj = True
                #check south west
                if row_num != max_row and place != max_col:
                    if not input_list[row_num+1][place+1].isnumeric() and input_list[row_num+1][place+1] != ".":
                        symb_adj = True
        else:
            if temp_num != "":
                if symb_adj:
                    part_nums.append(int(temp_num))
                    symb_adj = False
                temp_num = ""
        #Need to account for rows where num ends a line
        if place == max_col:
            if temp_num != "":
                if symb_adj:
                    part_nums.append(int(temp_num))
                    symb_adj = False
                temp_num = ""
total = 0
for part in part_nums:
    total += part

print(f'Part 1: {total}')