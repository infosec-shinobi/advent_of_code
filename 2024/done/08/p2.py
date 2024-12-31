grid = []
tracker = {}
antinodes = set()

def find_all_antinodes(max_cords, coord1, coord2):
    all_antinodes = []
    x1 = int(coord1[0])
    y1 = int(coord1[1])
    x2 = int(coord2[0])
    y2 = int(coord2[1])

    xslope = x2 - x1
    yslope = y2 - y1
    
    left_done = False
    right_done = False

    lsx = x1
    lsy = y1
    rsx = x2
    rsy = y2
    while not left_done:
        tx = lsx - xslope
        ty = lsy - yslope
        if (tx < 0 or tx > max_cords[0]) or (ty < 0 or ty > max_cords[1]):
            left_done = True
        else:
            all_antinodes.append((tx,ty))
            lsx = tx
            lsy = ty
    while not right_done:
        tx = rsx + xslope
        ty = rsy + yslope
        if (tx < 0 or tx > max_cords[0]) or (ty < 0 or ty > max_cords[1]):
            right_done = True
        else:
            all_antinodes.append((tx,ty))
            rsx = tx
            rsy = ty
    return all_antinodes

#with open('../../../input/2024/08/ex2.txt') as f:
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
                all_antinodes = find_all_antinodes(max_cords, item.split(","), peer.split(","))
                node1 = item.split(",")
                node2 = peer.split(",")
                antinodes.add((int(node1[0]),int(node1[1])))
                antinodes.add((int(node2[0]),int(node2[1])))
                for node in all_antinodes:
                    antinodes.add(node)
            tracker[freq][peer].append(item)
  
print(len(antinodes))