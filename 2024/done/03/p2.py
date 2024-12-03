import re

def valid_mem_commands(mem_str, mem_enabled, tracker):
    if mem_enabled:
        results = mem_str.split("don't()",1)
    else:
        results = mem_str.split("do()",1)
    tracker[str(mem_enabled)].append(results[0])
    if len(results) != 1:
        tracker = valid_mem_commands(results[1], not mem_enabled, tracker)
    return tracker

corrupted_memory = ""
mem_pattern = r'mul\(\b\d+\b\,\b\d+\b\)'
num_pattern = r'\b\d+\b'

#with open('../../../input/2024/03/ex.txt') as f:
with open('../../../input/2024/03/input.txt') as f:
    for line in f:
        corrupted_memory += line.strip()

mem_dict = {"True":[],
            "False":[]}

mem_dict = valid_mem_commands(corrupted_memory, True, mem_dict)

running_total = 0

for mem in mem_dict["True"]:
    good_mem = re.findall(mem_pattern, mem)
    for item in good_mem:
        temp = 1
        numbs = re.findall(num_pattern, item)
        for num in numbs:
            temp *= int(num)
        running_total += temp

print(running_total)
