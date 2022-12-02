from collections import Counter

template = ""
rules = {}

with open('ex.txt') as f:
#with open('input.txt') as f:

    for line in f:
        line = line.strip()

        if template == "":
            template = line
        elif line == "":
            continue
        else:
            pattern, value = line.split(" -> ")
            rules[pattern] = value

##########
# Part 1 #
##########

for x in range(0,10):
    print(x)
    temp_template = template[0]
    pair = ""
    #print(f"Current round: {x}, current template: {template}")
    for item in range(0, len(template)-1):
        pair = template[item]+template[item+1]
        if pair in rules:
            temp_template = temp_template + rules[pair] + pair[1]
        else:
            print("womp womp")
    template = temp_template

tracker = Counter(list(template))

min_count = min(tracker.values())
max_count = max(tracker.values())

print(f"max value ({max_count}) - min count ({min_count}) = {max_count-min_count}")

##########
# Part 2 #
##########

#can't use above code because to process intensive to track the string... start tracking the pairs themselves..
#print(f'Part 2: {increase_win}')