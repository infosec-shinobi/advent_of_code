from collections import deque

values = []

def get_next_move(input_data, r, c, visited):
    moves = []
    for move in [[r-1,c],[r+1,c],[r,c-1],[r,c+1]]:
        if move[0] < 0 or move[0] >= len(input_data) or move[1] < 0 or move[1] >= len(input_data[0]):
            continue
        elif (move[0], move[1]) in visited:
            continue
        else:
            moves.append(move)
    return moves

def bfs(input_data, s_row, s_col, g_row, g_col):
    tracking_queue = deque()
    tracking_queue.append((0, s_row, s_col))
    visited_tracker =[(s_row,s_col)]

    while len(tracking_queue) != 0:
        cur_depth, cur_row, cur_col = tracking_queue.popleft()
        next_steps = get_next_move(input_data, cur_row, cur_col, visited_tracker)
    
        for step in next_steps:
            cur_height = input_data[cur_row][cur_col]
            step_height = input_data[step[0]][step[1]]
            if (step[0], step[1]) in visited_tracker:
                continue
            if ord(step_height)-ord(cur_height) > 1:
                continue
            if step[0] == g_row and step[1] == g_col:
                return cur_depth+1

            visited_tracker.append((step[0], step[1]))
            tracking_queue.append((cur_depth+1, step[0], step[1]))


def bfs_p2(input_data, s_row, s_col, new_goal):
    tracking_queue2 = deque()
    tracking_queue2.append((0, s_row, s_col))
    visited_tracker2 =[(s_row,s_col)]

    while tracking_queue2:
        cur_depth, cur_row, cur_col = tracking_queue2.popleft()
        next_steps = get_next_move(input_data, cur_row, cur_col, visited_tracker2)
  
        for step in next_steps:
            cur_height = input_data[cur_row][cur_col]
            step_height = input_data[step[0]][step[1]]
            if (step[0], step[1]) in visited_tracker2:
                continue
            if ord(step_height)-ord(cur_height) < -1: # make sure the step difference is still only one away or a big fall
                continue
            if step_height == new_goal:
                return cur_depth+1
            visited_tracker2.append((step[0], step[1]))
            tracking_queue2.append((cur_depth+1, step[0], step[1]))

#with open('ex.txt') as f:
with open('input.txt') as f:
    for line in f:
        values.append(list(line.strip()))

##########
# Part 1 #
##########
total = 0

#find start and end positions
for row_num, row in enumerate(values):
    for col_num, item in enumerate(row):
        if item == "S":
            start_row = row_num
            start_col = col_num
            values[start_row][start_col] = "a"
        elif item == "E":
            goal_row = row_num
            goal_col = col_num
            values[goal_row][goal_col] = "z"
        else:
            continue

total = bfs(values, start_row, start_col, goal_row, goal_col)
print(f'Part 1: {total}')

##########
# Part 2 #
##########

total_2 = 0

total_2 = bfs_p2(values, goal_row, goal_col, "a")

print(f'Part 2: {total_2}')