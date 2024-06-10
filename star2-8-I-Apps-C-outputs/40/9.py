
N, M, alpha = map(int, input().split())
candies = [tuple(map(int, input().split())) for _ in range(M)]
candies = sorted(candies, key=lambda x: -x[2])
visited = [False] * (N+1)
visited[1] = True
result = 0
candies_bought = 0
while candies_bought < M:
    max_candy = 0
    max_index = 0
    for i, (u, v, c) in enumerate(candies):
        if visited[u] and not visited[v]:
            if max_candy < c:
                max_candy = c
                max_index = i
        elif visited[v] and not visited[u]:
            if max_candy < c:
                max_candy = c
                max_index = i
    if max_candy == 0:
        print("Poor girl")
        break
    result += max_candy**2 + alpha
    visited[u] = visited[v] = True
    candies_bought += 1
else:
    print(result)

