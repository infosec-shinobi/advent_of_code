from collections import Counter

hand_value = {}
strengths = {
            "5k": [],
            "4k": [],
            "fh": [],
            "3k": [],
            "2p": [],
            "1p": [],
            "other": []
            }

def get_hand_strengths(list_of_cards):
    """
    5k, 4k, fh, 3k, 2p, 1p, [akwjt9-2]
    """
    count_of_cards = Counter(list_of_cards)

    if max(count_of_cards.values()) == 5:
        strengths["5k"].append(list_of_cards)
    elif max(count_of_cards.values()) == 4:
        strengths["4k"].append(list_of_cards)
    elif max(count_of_cards.values()) == 3:
        card_sets = set(count_of_cards)
        if len(card_sets) == 2:
            strengths["fh"].append(list_of_cards)
        else:
            strengths["3k"].append(list_of_cards)
    else:
        card_sets = set(count_of_cards)
        if len(card_sets) == 3:
            strengths["2p"].append(list_of_cards)
        elif len(card_sets) == 4:
            strengths["1p"].append(list_of_cards)
        else:
            strengths["other"].append(list_of_cards)

def determine_best_card(hand_old, hand_new):
    scores = {"a":100,"k":90,"q":80,"j":70,"t":60,"9":50,"8":40,"7":30,"6":20,"5":10,"4":5,"3":2,"2":1}
    
    for card_num, old_card in enumerate(hand_old):
        if scores[old_card] == scores[hand_new[card_num]]:
            continue
        elif scores[old_card] > scores[hand_new[card_num]]:
            return False
        else:
            return True

#with open('ep1.txt') as f:
with open('i.txt') as f:
    for line in f:
        line = line.strip()
        hand = line.split()
        hand_value[hand[0].lower()] = int(hand[1])
        get_hand_strengths(hand[0].lower())

unprocesed_hands = len(hand_value)
total = 0

for key, value in strengths.items():
    temp_list = []
    if value == []:
        continue
    elif len(value) == 1:
        temp_list = value
    else:
        for hand in value:
            if temp_list == []:
                temp_list.append(hand)
            else:
                inserted = False
                for place, existing_hand in enumerate(temp_list):
                    bigger = determine_best_card(existing_hand, hand)
                    if bigger:
                        temp_list.insert(place, hand)
                        inserted = True
                        break
                if not inserted:
                    temp_list.append(hand)

    for item in temp_list:
        value = hand_value[item]
        add_value = value*unprocesed_hands
        total += add_value
        unprocesed_hands -= 1

print(f'Part 1: {total}')
