
def find_max_flowers(N, R, C, flowers):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def dfs(row, col, prev_petals):
        max_flowers = 1
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < N and 0 <= new_col < N and abs(new_row - row) + abs(new_col - col) > 1 \
                and flowers[new_row][new_col] > prev_petals:
                max_flowers = max(max_flowers, 1 + dfs(new_row, new_col, flowers[new_row][new_col]))
        
        return max_flowers

    return dfs(R-1, C-1, flowers[R-1][C-1])

# Reading input
N = int(input())
R, C = map(int, input().split())
flowers = []
for _ in range(N):
    flowers.append(list(map(int, input().split())))

# Calculate and print the result
print(find_max_flowers(N, R, C, flowers))
