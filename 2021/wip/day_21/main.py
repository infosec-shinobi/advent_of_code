p1_pos = 0
p2_pos = 0
count = 1

#with open('ex.txt') as f:
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        temp_values = line.split(": ")
        if count == 1:
            p1_pos = int(temp_values[1])
            count+=1
        else:
            p2_pos = int(temp_values[1])

##########
# Part 1 #
##########

def roll(player_position, dice_roll):
    total_moves = (dice_roll+1)+(dice_roll+2)+(dice_roll+3)    
    done_moving = False

    while not done_moving:
        if (10 - player_position) >= total_moves:
            player_position += total_moves
            done_moving = True
        elif total_moves > 10:
            total_moves -=10
        else:
            player_position = total_moves-(10 - player_position)
            done_moving = True
    return player_position, (dice_roll+3)

total = 0
p1_score = 0
p2_score = 0
last_dice_roll = 0

someone_won = False

while not someone_won:
    p1_pos, last_dice_roll = roll(p1_pos,last_dice_roll)
    p1_score += p1_pos
    if p1_score >= 1000:
        someone_won = True
    else:
        p2_pos, last_dice_roll = roll(p2_pos,last_dice_roll)
        p2_score += p2_pos
        if p2_score>=1000:
            someone_won = True
    total = min(p1_score,p2_score)*last_dice_roll
print(f'Part 1: {total}')

##########
# Part 2 #
##########

total_2 = 0

print(f'Part 2: {total_2}')