
MOD = 10**9 + 7

def dfs(u, parent, adj_list):
    global total_niceness

    white_paths = []
    black_paths = []

    for v in adj_list[u]:
        if v != parent:
            dfs(v, u, adj_list)
            white_paths.append(1 + white_paths[v])
            black_paths.append(1 + black_paths[v])

    if not white_paths:
        white_paths = [0]
    if not black_paths:
        black_paths = [0]

    max_white = max(white_paths)
    max_black = max(black_paths)

    total_niceness = (total_niceness + max(max_white, max_black)) % MOD

N = int(input())
adj_list = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = map(int, input().split())
    adj_list[a-1].append(b-1)
    adj_list[b-1].append(a-1)

total_niceness = 0
dfs(0, -1, adj_list)
print(total_niceness)
```
