
def can_jump(previous_petals, current_petals):
    return current_petals > previous_petals

def dfs(visited, flowers, row, col):
    visited[row][col] = True
    max_flowers = 1
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(flowers) and 0 <= new_col < len(flowers[0]) and not visited[new_row][new_col] and can_jump(flowers[row][col], flowers[new_row][new_col]):
            max_flowers = max(max_flowers, 1 + dfs(visited, flowers, new_row, new_col))
    
    visited[row][col] = False
    return max_flowers

def calculate_max_flowers(N, R, C, flowers):
    visited = [[False for _ in range(N)] for _ in range(N)]
    return dfs(visited, flowers, R-1, C-1)

# Reading input
N = int(input())
R, C = map(int, input().split())
flowers = [list(map(int, input().split())) for _ in range(N)]

# Calculate and print the result
result = calculate_max_flowers(N, R, C, flowers)
print(result)
