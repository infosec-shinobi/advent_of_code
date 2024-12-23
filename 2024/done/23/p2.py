connections = {}
current_pwd = ()
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

possible_conns = set()
for k,v in connections.items():
    for peer in v:
        peer_peers = connections[peer]
        intersection = (v.intersection(peer_peers))
        temp_list = [k, peer]
        for item in intersection:
            temp_list.append(item)
        possible_conns.add(tuple(sorted(temp_list)))

for conn in possible_conns:
    if len(conn) > len(current_pwd):
        all_peers = True
        for item in conn:
            current_peers = connections[item]
            for item2 in conn:
                if item2 not in current_peers and item2 != item:
                    all_peers = False
        if all_peers:
            current_pwd = conn

print(','.join(current_pwd))
