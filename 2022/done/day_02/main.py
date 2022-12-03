hands = []
lookups = {"A": "rock", "X": "rock", "B": "paper", "Y": "paper", "C": "scissors", "Z": "scissors"}
scores = {"win": 6, "lost": 0, "draw": 3, "rock": 1, "paper": 2, "scissors": 3}

#with open('ex.txt') as f:
with open('input.txt') as f:
    for line in f:
        temp_list = []
        line = line.strip()
        temp_list = line.split()
        hands.append(temp_list)

##########
# Part 1 #
##########

score_card = []

for rnd in hands:
    tmp_score = 0
    elf_pick = lookups[rnd[0]]
    my_pick = lookups[rnd[1]]
    tmp_score += scores[my_pick]
 
    if elf_pick == my_pick:
        #draw
        tmp_score += scores["draw"]
    elif my_pick == "rock" and elf_pick == "scissors" or my_pick == "scissors" and elf_pick == "paper" or my_pick == "paper" and elf_pick == "rock":
        #win
        tmp_score += scores["win"]
    else:
        #draw, 0 additional points
        pass
    score_card.append(tmp_score)

print(f'Part 1: {sum(score_card)}')

##########
# Part 2 #
##########

total_2 = 0
lookups = {"A": "rock", "X": "lose", "B": "paper", "Y": "draw", "C": "scissors", "Z": "win"}
scores = {"win": 6, "lost": 0, "draw": 3, "rock": 1, "paper": 2, "scissors": 3}

score_card = []

for rnd in hands:
    tmp_score = 0
    elf_pick = lookups[rnd[0]]
    outcome = lookups[rnd[1]]
     
    if outcome == "draw": 
        #draw
        tmp_score = scores["draw"] + scores[elf_pick]
    elif outcome == "lose":
        tmp_score = scores["lost"]
        if elf_pick == "scissors":
            tmp_score += scores["paper"]
        elif elf_pick == "paper":
            tmp_score += scores["rock"]
        else:
             tmp_score += scores["scissors"]
    else:
        tmp_score = scores["win"]
        if elf_pick == "scissors":
            tmp_score += scores["rock"]
        elif elf_pick == "paper":
            tmp_score += scores["scissors"]
        else:
             tmp_score += scores["paper"]
    score_card.append(tmp_score)

print(f'Part 2: {sum(score_card)}')