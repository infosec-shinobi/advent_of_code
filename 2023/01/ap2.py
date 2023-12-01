input_list = []
valid_nums = {"one":"1",
              "two":"2",
              "three":"3",
              "four":"4",
              "five":"5",
              "six":"6",
              "seven":"7",
              "eight":"8",
              "nine":"9"}

def find_num(search_list,lookup_dic, side):
    temp_value = ""
    found_value = False
    for item in search_list:
        if side == "l":
            temp_value = temp_value + item
        else:
            temp_value = item + temp_value
        for key in lookup_dic.keys():
            if key in temp_value:
                found_value = lookup_dic[key]
                break
        if found_value:
            break
        if item.isnumeric():
            found_value = str(item)
            break
    return found_value
#with open('ep2.txt') as f:
with open('i.txt') as f:
    for line in f:
        line = line.strip()
        input_list.append(list(line))

line_nums = []
for line in input_list:
    r_list = reversed(line)
    l = find_num(line,valid_nums, "l")
    r = find_num(r_list,valid_nums, "r")
    line_nums.append(int(l+r))

total = 0
for num in line_nums:
    total += num
print(f'Part 2: {total}')