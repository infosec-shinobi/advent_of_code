input_list = []
#with open('ep1.txt') as f:
with open('i.txt') as f:
    for line in f:
        line = line.strip()
        input_list.append(line)

game_power = []

for line in input_list:
    cube_min = {"red":0,
                "blue":0,
                "green":0}
    game, data = line.split(": ")
    _, game_num = game.split(" ")
    game_sets = data.split("; ")
    for single_set in game_sets:
        cubes = single_set.split(", ")
        for cube in cubes:
            cube_count, cube_color = cube.split(" ")
            if int(cube_count) > cube_min[cube_color]:
                cube_min[cube_color] = int(cube_count)

    game_power.append(cube_min["red"]*cube_min["blue"]*cube_min["green"])

total = 0
for game in game_power:
    total += game

print(f'Part 1: {total}')