
def tetris_ways(C, P, heights):
    piece_heights = [[-1, 0], [0, -1], [0, 0], [0, 1], [1, 0], [-1, 0], [0, 0]]
    
    def valid_position(row, col):
        if row < 0 or col < 0 or row >= len(board) or col >= C:
            return False
        return True
    
    def can_place_piece(row, col):
        for i in range(4):
            new_row = row + piece_heights[P-1][i]
            new_col = col + piece_heights[P-1][i+4]
            if not valid_position(new_row, new_col) or board[new_row][new_col] != 0:
                return False
        return True
    
    def place_piece(row, col):
        for i in range(4):
            new_row = row + piece_heights[P-1][i]
            new_col = col + piece_heights[P-1][i+4]
            board[new_row][new_col] = 1
    
    def remove_piece(row, col):
        for i in range(4):
            new_row = row + piece_heights[P-1][i]
            new_col = col + piece_heights[P-1][i+4]
            board[new_row][new_col] = 0
    
    def count_ways(row):
        if row == len(board):
            return 1
        
        total_ways = 0
        for col in range(C):
            if can_place_piece(row, col):
                place_piece(row, col)
                total_ways += count_ways(row + 1)
                remove_piece(row, col)
        
        return total_ways
    
    board = [[0 for _ in range(C)] for _ in range(max(heights))]
    for col, height in enumerate(heights):
        for i in range(height):
            board[i][col] = 1
    
    return count_ways(0)

# Reading input
C, P = map(int, input().split())
heights = list(map(int, input().split()))

# Calculate and print the number of ways
print(tetris_ways(C, P, heights))
```
