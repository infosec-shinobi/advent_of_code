# https://adventofcode.com/2020/day/22
# --- Day 22: Crab Combat ---

def main():
    #open input file
    f = open("input.txt", "r")

    input_list = []
    player1_hand = []
    player2_hand = []
    current = "p1"

    #read each line and add to list
    for x in f:
        x = x.strip()
        if x == "Player 2:":
            current = "p2"
        elif x == "Player 1:" or x == "":
            continue #do nothing
        else:
            if current == "p1":
                player1_hand.append(int(x.strip()))
            else:
                player2_hand.append(int(x.strip()))
    print(f"p1 hand:\n{player1_hand}")
    print(f"p2 hand:\n{player2_hand}")

    game_over = False
    round_count = 1
    while not game_over:
        if len(player1_hand) == 0:
            winner = player2_hand
            print(f"p2 wins! Hand is:\n{player2_hand}")
            game_over = True
        elif len(player2_hand) == 0:
            winner = player1_hand
            print(f"p1 wins! Hand is:\n{player1_hand}")
            game_over = True
        else:
            print(f"Round {round_count}!")
            p1_card = player1_hand[0]
            p2_card = player2_hand[0]
            player1_hand.pop(0)
            player2_hand.pop(0)

            if p1_card > p2_card:
                print(f"p1 wins, {p1_card} beats {p2_card}")
                player1_hand.append(p1_card)
                player1_hand.append(p2_card)
            else:
                print(f"p2 wins, {p2_card} beats {p1_card}")
                player2_hand.append(p2_card)
                player2_hand.append(p1_card)
        round_count += 1

    win_len = len(winner)
    total = 0

    for x in winner:
        total += x*win_len
        win_len -= 1
    print(f"total is {total}")
if __name__ == "__main__":
    main()