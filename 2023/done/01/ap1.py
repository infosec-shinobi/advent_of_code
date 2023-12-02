input_list = []
#with open('ep1.txt') as f:
with open('i.txt') as f:
    for line in f:
        line = line.strip()
        input_list.append(list(line))
    
    #print(input_list)

line_nums = []
for line in input_list:
    #print(line)
    r_list = reversed(line)
    for item in line:
        if item.isnumeric():
            l = item
            break
    for item in r_list:
        if item.isnumeric():
            r = item
            break
    line_nums.append(int(l+r))
#print(line_nums)
total = 0
for num in line_nums:
    total += num
print(f'Part 1: {total}')