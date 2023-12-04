input_list = []
card_count = {}
#with open('ep2.txt') as f:
with open('i.txt') as f:
    count = 1
    for line in f:
        line = line.strip()
        input_list.append(line)
        card_count[count] = 1
        count += 1

for line in input_list:
    game, data = line.split(": ")
    _, game_num = game.split()
    win_nums, elfs_nums = data.split(" | ")
    win_nums_list = win_nums.split()
    elfs_nums_list = elfs_nums.split()
    additional_cards = sum(winning_num in elfs_nums_list for winning_num in win_nums_list)
    num_of_card_copies =  card_count[int(game_num)]
    for card in range(1, additional_cards+1):
        card_count[int(game_num)+card] += num_of_card_copies

total = 0

for _, num_of_cards in card_count.items():
    total += num_of_cards
print(f'Part 2: {total}')