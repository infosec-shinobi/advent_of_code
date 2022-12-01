
BINARY_CONVERSION = {
    "0":"0000",
    "1":"0001",
    "2":"0010",
    "3":"0011",
    "4":"0100",
    "5":"0101",
    "6":"0110",
    "7":"0111",
    "8":"1000",
    "9":"1001",
    "A":"1010",
    "B":"1011",
    "C":"1100",
    "D":"1101",
    "E":"1110",
    "F":"1111"
    }

values = []

with open('ex.txt') as f:
#with open('input.txt') as f:
    for line in f:
        line = line.strip()
        values.append(line)

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