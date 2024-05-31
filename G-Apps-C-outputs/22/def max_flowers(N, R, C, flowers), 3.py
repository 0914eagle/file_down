
def max_flowers(N, R, C, flowers):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def dfs(r, c, prev_petals, visited):
        if r < 0 or r >= N or c < 0 or c >= N or visited[r][c] or flowers[r][c] <= prev_petals:
            return 0
        
        visited[r][c] = True
        max_flowers_count = 1
        
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            max_flowers_count = max(max_flowers_count, 1 + dfs(new_r, new_c, flowers[r][c], visited))
            
        visited[r][c] = False
        return max_flowers_count
    
    visited = [[False for _ in range(N)] for _ in range(N)]
    return dfs(R-1, C-1, 0, visited)

# Read input
N = int(input())
R, C = map(int, input().split())
flowers = []
for _ in range(N):
    row = list(map(int, input().split()))
    flowers.append(row)

# Calculate and print the result
result = max_flowers(N, R, C, flowers)
print(result)
