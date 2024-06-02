
def count_wall_segments(R, C, wall):
    def is_brick(r, c):
        return wall[R - r][c] == 'B'
    
    def is_valid_position(r, c):
        return 0 <= r < R and 0 <= c < C
    
    def dfs(r, c):
        stack = [(r, c)]
        visited.add((r, c))
        
        while stack:
            curr_r, curr_c = stack.pop()
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_r, new_c = curr_r + dr, curr_c + dc
                
                if is_valid_position(new_r, new_c) and is_brick(new_r, new_c) and (new_r, new_c) not in visited:
                    stack.append((new_r, new_c))
                    visited.add((new_r, new_c))
    
    visited = set()
    segments = 0
    
    for r in range(R):
        for c in range(C):
            if is_brick(r, c) and (r, c) not in visited:
                dfs(r, c)
                segments += 1
    
    return segments

# Input parsing
R, C = map(int, input().split())
wall = [input() for _ in range(R)]

# Output
print(count_wall_segments(R, C, wall))
