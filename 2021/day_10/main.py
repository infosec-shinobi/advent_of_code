values = []

with open('ex.txt') as f:
#with open('input.txt') as f:
    for line in f:
        line = line.strip()
        temp_list = []
        for symbol in line:
            temp_list.append(symbol)
        values.append(temp_list)

##########
# Part 1 #
##########
total = 0

p1_lookup_v = {')':3,']':57,'}':1197,'>':25137}
open_sym = ['(','[','{','<']

for item in values:
    temp_list = []
    corrupt = False
    print(item)
    for place in range(0,len(item)-1):
        symbol = item[place]
        if symbol in open_sym:
            print("appending")
            temp_list.append(symbol)
        else:
            print("popping")
            if symbol == ")":
                if symbol == temp_list[-1]:
                    temp_list.pop
                else:
                    corrupt = True
                    break
            elif symbol == "]":
                if symbol == temp_list[-1]:
                    temp_list.pop
                else:
                    corrupt = True
                    break
            elif symbol == "}":
                if symbol == temp_list[-1]:
                    temp_list.pop
                else:
                    corrupt = True
                    break
            else:
                if symbol == temp_list[-1]:
                    temp_list.pop
                else:
                    corrupt = True
                    break
    if corrupt:
        print(f'{symbol} detected')
        total += p1_lookup_v[symbol]

print(f'Part 1: {total}')

##########
# Part 2 #
##########


part_2_total = 0


print(f'Part 2: {part_2_total}')