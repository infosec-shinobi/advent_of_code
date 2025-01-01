from itertools import product

data = []

def evaluate_eq(num_list, operators):
    current = num_list[0]
    for i in range(1, len(num_list)):
        if operator_list[i-1] == "+":
            current += num_list[i]
        else:
            current *= num_list[i]
    return current

#with open('../../../input/2024/07/ex.txt') as f:
with open('../../../input/2024/07/input.txt') as f:
    for line in f:
        temp_list = line.strip().split(":")
        final_list = []
        final_list.append(int(temp_list[0]))
        final_list.append([int(x) for x in temp_list[1].strip().split(" ")])
        data.append(final_list)

ans = 0
for line in data:
    for operator_list in product("*+", repeat=(len(line[1])-1)):
        if line[0] == evaluate_eq(line[1], operator_list):
            ans += line[0]
            break

print(ans)