
def shortest_ladder_length(M, N, vault):
    def is_valid(ladder_length):
        visited = [[False for _ in range(N)] for _ in range(M)]
        queue = [(0, 0)]
        while queue:
            i, j = queue.pop(0)
            if i == M - 1 and j == N - 1:
                return True
            visited[i][j] = True
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_i, new_j = i + x, j + y
                if 0 <= new_i < M and 0 <= new_j < N and not visited[new_i][new_j] and abs(vault[new_i][new_j] - vault[i][j]) <= ladder_length:
                    queue.append((new_i, new_j))
        return False

    left, right = 0, 10**9
    while left < right:
        mid = (left + right) // 2
        if is_valid(mid):
            right = mid
        else:
            left = mid + 1
    return left

# Input
M, N = map(int, input().split())
vault = [list(map(int, input().split())) for _ in range(M)]

# Output
print(shortest_ladder_length(M, N, vault))
```
