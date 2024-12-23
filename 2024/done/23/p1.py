connections = {}

#with open('../../../input/2024/23/ex.txt') as f:
with open('../../../input/2024/23/input.txt') as f:
    for line in f:
        temp_list = line.strip().split("-")
        if temp_list[0] not in connections:
            connections[temp_list[0]] = set()
        if temp_list[1] not in connections:
            connections[temp_list[1]] = set()
        connections[temp_list[0]].add(temp_list[1])
        connections[temp_list[1]].add(temp_list[0])

three_connect = set()
for k,v in connections.items():
    for peer in v:
        peer_peers = connections[peer]
        intersection = (v.intersection(peer_peers))
        for item in intersection:
            three_connect.add(tuple(sorted([k, peer, item])))

final_list = set()
for item in three_connect:
    for computer in item:
        if computer.startswith("t"):
            final_list.add(item)
print(len(final_list))