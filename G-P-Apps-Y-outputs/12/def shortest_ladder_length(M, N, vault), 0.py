
def shortest_ladder_length(M, N, vault):
    def dfs(x, y, ladder_len):
        nonlocal min_ladder_len
        if x == M-1 and y == N-1:
            min_ladder_len = min(min_ladder_len, ladder_len)
            return
        
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                climb = max(0, vault[nx][ny] - vault[x][y])
                new_ladder_len = max(ladder_len, climb)
                dfs(nx, ny, new_ladder_len)
                visited[nx][ny] = False

    min_ladder_len = float('inf')
    visited = [[False for _ in range(N)] for _ in range(M)]
    visited[0][0] = True
    dfs(0, 0, 0)
    return min_ladder_len

# Input parsing
input_lines = input().split('\n')
M, N = map(int, input_lines[0].split())
vault = [[int(x) for x in line.split()] for line in input_lines[1:M+1]]

result = shortest_ladder_length(M, N, vault)
print(result)
```
