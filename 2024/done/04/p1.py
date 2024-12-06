import re
target = "XMAS"
target2 = "SAMX"

def find_target(list_of_strings):
    total = 0
    for item in list_of_strings:
        #print(item)
        total += len(re.findall(target, item))
        total += len(re.findall(target2, item))
        #print(total)
    return total

def n_to_south(list_of_strings):
    new_grid = []
    for item in list_of_strings:
        if new_grid == []:
            for letter in item:
                new_grid.append([letter])
        else:
            for index,letter in enumerate(item):
                new_grid[index].append(letter)
    string_grid = []
    for item in new_grid:
        temp_str = ""
        for letter in item:
            temp_str += letter
        string_grid.append(temp_str)
    return string_grid

def rdiagonal(list_of_strings):
    new_grid = []
    num_of_strings = len(list_of_strings)
    str_length = len(list_of_strings[0])
    total_diagonals = str_length + (num_of_strings-1)

    for list_index, item in enumerate(list_of_strings):
        temp_value = ""
        if new_grid == []:
            for index, letter in enumerate(item):
                start = 0
                for x in range(index,str_length):
                    temp_value += list_of_strings[start][x]
                    start +=1
                new_grid.append(temp_value)
                temp_value = ""
        else:
            start = list_index
            for x in range(0,(str_length-list_index)):
                temp_value += list_of_strings[start][x]
                start += 1
            new_grid.append(temp_value)
    return new_grid

def ldiagonal(list_of_strings):
    new_grid = []
    num_of_strings = len(list_of_strings)
    str_length = len(list_of_strings[0])
    total_diagonals = str_length + (num_of_strings-1)

    temp_grid = []
    for item in list_of_strings:
        temp_grid.append(item[::-1])
    for list_index, item in enumerate(temp_grid):
        temp_value = ""
        if new_grid == []:
            for index, letter in enumerate(item):
                start = 0
                for x in range(index,str_length):
                    temp_value += temp_grid[start][x]
                    start +=1
                new_grid.append(temp_value)
                temp_value = ""
        else:
            start = list_index
            for x in range(0,(str_length-list_index)):
                temp_value += temp_grid[start][x]
                start += 1
            new_grid.append(temp_value)
    return new_grid

grid = []
#with open('../../../input/2024/04/ex.txt') as f:
with open('../../../input/2024/04/input.txt') as f:
    for line in f:
        temp_list = line.strip()
        grid.append(temp_list)

#print(grid)

targets_found = 0

#left to right
targets_found += find_target(grid)

#north to south
targets_found += find_target(n_to_south(grid))

#right diagonal
targets_found += find_target(rdiagonal(grid))

#left diagonal
targets_found += find_target(ldiagonal(grid))

print(targets_found)