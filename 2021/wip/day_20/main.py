values = []
algo = []
line_count = 0
with open('ex.txt') as f:
#with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if line_count == 0:
            for item in line:
                algo.append(item)
                line_count+=1
        elif line == "":
            continue
        else:
            temp_list = []
            for item in line:
                temp_list.append(item)
            values.append(temp_list)

print(algo)
print(" ")
print(values)

##########
# Part 1 #
##########
total = 0

print(f'Part 1: {total}')

##########
# Part 2 #
##########

total_2 = 0

print(f'Part 2: {total_2}')