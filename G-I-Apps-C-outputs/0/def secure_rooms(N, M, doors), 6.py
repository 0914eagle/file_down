
def secure_rooms(N, M, doors):
    adj_list = [[] for _ in range(N)]
    for u, v in doors:
        if u == -1 or v == -1:
            continue
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    visited = [False] * N
    ans = 0
    for i in range(N):
        if not visited[i]:
            q = [i]
            visited[i] = True
            count = 1
            while q:
                current = q.pop()
                for neighbor in adj_list[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        q.append(neighbor)
                        count += 1
            ans = max(ans, count)
    
    return ans - 1

# Sample Input
N = 2
M = 3
doors = [(-1, 0), (-1, 1), (0, 1)]

# Output
print(secure_rooms(N, M, doors))
```
