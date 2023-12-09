input_list = []
with open('ep2.txt') as f:
#with open('i.txt') as f:
    for line in f:
        line = line.strip()
        input_list.append(line)

print(input_list)

total = 0

print(f'Part 2: {total}')