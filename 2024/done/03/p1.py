import re

corrupted_memory = []
clean_memory = []
mem_pattern = r'mul\(\b\d+\b\,\b\d+\b\)'
num_pattern = r'\b\d+\b'

#with open('../../../input/2024/03/ex.txt') as f:
with open('../../../input/2024/03/input.txt') as f:
    for line in f:
        corrupted_memory.append(line)
        clean_memory.extend(re.findall(mem_pattern, line))

print(clean_memory)

running_total = 0
for uncorrupted_mem in clean_memory:
    temp = 1
    numbs = re.findall(num_pattern, uncorrupted_mem)
    for num in numbs:
        temp *= int(num)
    running_total += temp

print(running_total)
