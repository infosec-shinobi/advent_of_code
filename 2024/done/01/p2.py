l_list = []
r_list = []

#with open('../../../input/2024/01/ex.txt') as f:
with open('../../../input/2024/01/input.txt') as f:
    for line in f:
        line = line.strip().split()
        l_list.append(int(line[0]))
        r_list.append(int(line[1]))

l_sorted = sorted(l_list)
r_sorted = sorted(r_list)

total_distance = 0
for num in l_sorted:
    total_distance += num * r_sorted.count(num)

print(total_distance)