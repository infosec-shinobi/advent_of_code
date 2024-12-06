grid = []

guard_tracker = []
guard_position = []
guard_direction = "N"

def print_grid(grid):
    for line in grid:
        print(line)
    print("\n")

def move_guard(grid, guard_direction, guard_position, max_col, max_row):
    move = {
        "N": [-1, 0, "E"],
        "E": [ 0, 1, "S"],
        "S": [1, 0, "W"],
        "W": [ 0,-1, "N"]
    }
    guard_col = guard_position[0]
    guard_row = guard_position[1]
    next_spot = ""
    if (guard_col == 0 and guard_direction == "N") or (guard_row == 0 and guard_direction == "W") or (guard_col == max_col and guard_direction == "S") or (guard_row == max_row and guard_direction == "E"):
        return [["done","done"], guard_direction]
    else:
        next_spot = grid[guard_position[0]+move[guard_direction][0]][guard_position[1]+move[guard_direction][1]]
        if next_spot == "#":
            return [[guard_position[0], guard_position[1]], move[guard_direction][2]]
        else:
            return [[guard_position[0]+move[guard_direction][0],guard_position[1]+move[guard_direction][1]], guard_direction]

#with open('../../../input/2024/06/ex.txt') as f:
with open('../../../input/2024/06/input.txt') as f:
    cur_column = 0
    for line in f:
        cur_row = 0        
        for item in line.strip():
            if item == "^":
                guard_tracker.append([cur_column,cur_row])
                guard_position = [cur_column, cur_row]

            cur_row += 1
        cur_column += 1
        grid.append(line.strip())

done = False

count = 1
while not done:
    results = move_guard(grid, guard_direction, guard_position, cur_column-1, cur_row-1)
    if results[0][0] == "done":
        if [guard_position[0],guard_position[1]] not in guard_tracker:
            guard_tracker.append([guard_position[0],guard_position[1]])
        done = True
    else:
        if guard_position == results[0]:
            guard_direction = results[1]
        else:
            if [guard_position[0],guard_position[1]] not in guard_tracker:
                guard_tracker.append([guard_position[0],guard_position[1]])
            guard_position = results[0]
    count += 1

print(len(guard_tracker))