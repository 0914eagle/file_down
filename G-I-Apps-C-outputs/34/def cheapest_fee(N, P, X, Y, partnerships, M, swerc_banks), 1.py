
def cheapest_fee(N, P, X, Y, partnerships, M, swerc_banks):
    connections = {}
    for a, b, c in partnerships:
        if a not in connections:
            connections[a] = {}
        if b not in connections:
            connections[b] = {}
        connections[a][b] = c
        connections[b][a] = c

    swerc_set = set(swerc_banks)
    queue = [(X, 0)]

    while queue:
        cur_bank, cur_fee = queue.pop(0)
        
        if cur_bank == Y:
            return cur_fee
        
        for next_bank, fee in connections[cur_bank].items():
            if next_bank not in swerc_set:
                queue.append((next_bank, max(cur_fee, fee)))

    return "Impossible"

N, P, X, Y = map(int, input().split())
partnerships = [tuple(map(int, input().split())) for _ in range(P)]
M = int(input())
swerc_banks = list(map(int, input().split()))

result = cheapest_fee(N, P, X, Y, partnerships, M, swerc_banks)
print(result)
```
