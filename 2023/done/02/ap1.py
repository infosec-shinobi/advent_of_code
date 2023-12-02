max_cubes = {"red": 12,
             "green": 13,
             "blue": 14
            }
input_list = []
#with open('ep1.txt') as f:
with open('i.txt') as f:
    for line in f:
        line = line.strip()
        input_list.append(line)
valid_games = []

for line in input_list:
    valid = True

    game, data = line.split(": ")
    _, game_num = game.split(" ")
    game_sets = data.split("; ")
    for single_set in game_sets:
        cubes = single_set.split(", ")
        for cube in cubes:
            cube_count, cube_color = cube.split(" ")
            if int(cube_count) > max_cubes[cube_color]:
                valid = False
    if valid:
        valid_games.append(int(game_num))

total = 0
for game in valid_games:
    total += game

print(f'Part 1: {total}')