
def find_tour(N, M):
    if N * M % 2 != 0:
        return -1
    
    grid = [[0 for _ in range(M)] for _ in range(N)]
    
    def valid_move(r, c):
        return 0 <= r < N and 0 <= c < M and grid[r][c] == 0
    
    def move(r, c, step):
        grid[r][c] = step
        if step == N * M:
            return True
        
        possible_moves = [(r+2, c+1), (r+2, c-1), (r-2, c+1), (r-2, c-1),
                          (r+1, c+2), (r+1, c-2), (r-1, c+2), (r-1, c-2)]
        
        for row, col in possible_moves:
            if valid_move(row, col) and move(row, col, step+1):
                return True
        
        grid[r][c] = 0
        return False
    
    start_r, start_c = 0, 0
    if not move(start_r, start_c, 1):
        return -1

    return grid

# Input
N, M = map(int, input().split())

# Output
result = find_tour(N, M)
if result == -1:
    print(-1)
else:
    for row in result:
        for col in row:
            print(row.index(col) + 1, col + 1)
