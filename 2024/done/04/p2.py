def find_target(data):
    ms00 = data[0][0]
    ms02 = data[0][2]
    a1 = data[1][1]
    ms20 = data[2][0]
    ms22 = data[2][2]

    if a1 != "A":
        return 0
    else:
        valid_strings = ["MMSS", "MSMS", "SSMM", "SMSM"]
        temp = ms00+ms02+ms20+ms22
        if temp in valid_strings:
            return 1
        else:
            return 0

grid = []
#with open('../../../input/2024/04/ex.txt') as f:
with open('../../../input/2024/04/input.txt') as f:
    for line in f:
        temp_list = line.strip()
        grid.append(temp_list)

targets_found = 0
if len(grid) > 0:
    grid_width = len(grid[0])
    grid_height = len(grid)
else:
    print("Bad input")
    exit

for index, row in enumerate(grid):
    if grid_height - index > 2:
        for index2, item in enumerate(row):
            if grid_width - index2 > 2:
                temp_grid = []
                temp_grid.append(grid[index][index2:index2+3])
                temp_grid.append(grid[index+1][index2:index2+3])
                temp_grid.append(grid[index+2][index2:index2+3])
                targets_found += find_target(temp_grid)

print(targets_found)