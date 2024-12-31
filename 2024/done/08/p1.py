grid = []
tracker = {}
antinodes = set()

def find_antinodes(max_cords, coord1, coord2):
    
    antinode1x = int(coord1[0]) - (int(coord2[0])-int(coord1[0]))
    antinode1y = int(coord1[1]) - (int(coord2[1])-int(coord1[1]))
    antinode2x = int(coord2[0]) + (int(coord2[0])-int(coord1[0]))
    antinode2y = int(coord2[1]) + (int(coord2[1])-int(coord1[1]))
    if (antinode1x < 0 or antinode1x > max_cords[0]) or (antinode1y < 0 or antinode1y > max_cords[1]):
        a1 = None
    else:
        a1 = (antinode1x, antinode1y)
    if (antinode2x < 0 or antinode2x > max_cords[0]) or (antinode2y < 0 or antinode2y > max_cords[1]):
        a2 = None
    else:
        a2 = (antinode2x, antinode2y)
    return a1, a2

#with open('../../../input/2024/08/ex.txt') as f:
with open('../../../input/2024/08/input.txt') as f:
    count = 0 
    for line in f:
        temp_list = list(line.strip())
        for index, item in enumerate(temp_list):
            if item != ".":
                if item not in tracker:
                    tracker[item] = {f"{count},{index}": []}
                else:
                    tracker[item].update({f"{count},{index}": []})
        count += 1
        grid.append(temp_list)

max_cords = [len(grid[0])-1, len(grid)-1]

for freq, known_peers in tracker.items():
    values = list(known_peers.keys())
    for item in values:
        checked_peers = tracker[freq][item]
        for peer in values:
            if item != peer and peer not in checked_peers:
                a1, a2 = find_antinodes(max_cords, item.split(","), peer.split(","))
                if a1:
                    antinodes.add(a1)
                if a2:
                    antinodes.add(a2)
            tracker[freq][peer].append(item)
  
print(len(antinodes))
