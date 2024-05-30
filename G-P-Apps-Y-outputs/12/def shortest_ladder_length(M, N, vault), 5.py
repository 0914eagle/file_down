
def shortest_ladder_length(M, N, vault):
    def is_valid(ladder_length):
        visited = set()
        stack = [(0, 0)]
        while stack:
            x, y = stack.pop()
            if x == M-1 and y == N-1:
                return True
            visited.add((x, y))
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < M and 0 <= ny < N and (nx, ny) not in visited:
                    height_diff = abs(vault[nx][ny] - vault[x][y])
                    if height_diff <= ladder_length:
                        stack.append((nx, ny))
        return False
    
    left, right = 0, 10**9
    while left < right:
        mid = (left + right) // 2
        if is_valid(mid):
            right = mid
        else:
            left = mid + 1
    return left

# Parse input
input_line = input().split()
M, N = int(input_line[0]), int(input_line[1])
vault = []
for _ in range(M):
    vault.append(list(map(int, input().split())))

# Call the function and print the result
print(shortest_ladder_length(M, N, vault))
```
