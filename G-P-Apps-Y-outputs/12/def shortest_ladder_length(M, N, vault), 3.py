
def shortest_ladder_length(M, N, vault):
    def is_valid_path(h):
        visited = set()
        stack = [(0, 0)]
        while stack:
            i, j = stack.pop()
            if i == M - 1 and j == N - 1:
                return True
            visited.add((i, j))
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= ni < M and 0 <= nj < N and (ni, nj) not in visited and abs(vault[ni][nj] - vault[i][j]) <= h:
                    stack.append((ni, nj))
        return False

    low, high = 0, max(vault[-1][-1], vault[0][0])
    while low < high:
        mid = low + (high - low) // 2
        if is_valid_path(mid):
            high = mid
        else:
            low = mid + 1
    return low

# Read input
M, N = map(int, input().split())
vault = [list(map(int, input().split())) for _ in range(M)]

# Call the function and output the result
print(shortest_ladder_length(M, N, vault))
```
