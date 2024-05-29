
def find_largest_fee(N, P, X, Y, partnerships, M, SWERC_banks):
    def bfs(adj_list, start, end, max_fee):
        queue = [[start, max_fee]]
        visited = set()
        visited.add(start)
        
        while queue:
            current, current_fee = queue.pop(0)
            
            if current == end:
                return True
            
            for neighbor, fee in adj_list[current]:
                if (neighbor, current_fee) not in visited and fee <= current_fee:
                    visited.add((neighbor, current_fee))
                    queue.append([neighbor, current_fee])
        
        return False

    adj_list = {i: [] for i in range(1, N + 1)}
    
    for a, b, c in partnerships:
        adj_list[a].append((b, c))
        adj_list[b].append((a, c))
    
    SWERC_banks_set = set(SWERC_banks)
    
    min_fee = float('inf')
    
    for i in range(P):
        a, b, c = partnerships[i]
        if (a in SWERC_banks_set and b in SWERC_banks_set) or (a == X and b in SWERC_banks_set) or (b == Y and a in SWERC_banks_set):
            min_fee = min(min_fee, c)
    
    if min_fee == float('inf'):
        return "Impossible"
    
    max_fee = min_fee
    while bfs(adj_list, X, Y, max_fee):
        max_fee += 1
    
    return max_fee if max_fee != float('inf') else "Infinity"

# Sample Input 1
N1 = 6
P1 = 8
X1 = 1
Y1 = 6
partnerships1 = [[1, 2, 5], [1, 3, 1], [2, 6, 6], [2, 3, 6], [4, 2, 3], [3, 4, 1], [4, 5, 1], [5, 6, 1]]
M1 = 5
SWERC_banks1 = [1, 3, 6, 5, 4]
print(find_largest_fee(N1, P1, X1, Y1, partnerships1, M1, SWERC_banks1))  # Output: 3

# Sample Input 2
N2 = 3
P2 = 4
X2 = 1
Y2 = 2
partnerships2 = [[1, 2, 6], [1, 3, 2], [1, 2, 7], [2, 3, 3]]
M2 = 2
SWERC_banks2 = [1, 2]
print(find_largest_fee(N2, P2, X2, Y2, partnerships2, M2, SWERC_banks2))  # Output: Infinity
```
