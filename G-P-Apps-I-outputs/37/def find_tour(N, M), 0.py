
def find_tour(N, M):
    if N == 1 and M == 1:
        print("1 1")
        return
    
    if N == 1 or M == 1 or (N == 2 and M == 2):
        print("-1")
        return
    
    grid = [[0 for _ in range(M)] for _ in range(N)]
    directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    row = 0
    col = 0
    grid[row][col] = 1
    count = 1
    
    while count < N*M:
        next_moves = []
        for move in moves:
            next_row = row + move[0]
            next_col = col + move[1]
            if 0 <= next_row < N and 0 <= next_col < M and grid[next_row][next_col] == 0:
                count += 1
                grid[next_row][next_col] = count
                next_moves.append((next_row, next_col))
        
        if len(next_moves) == 0:
            print("-1")
            return
        
        row, col = next_moves[0]
    
    for i in range(N):
        for j in range(M):
            print(i+1, j+1)
    
N, M = map(int, input().split())
find_tour(N, M)
