
def tetris_ways(columns, piece, heights):
    piece_matrix = []
    if piece == 1:
        piece_matrix = [[1, 1, 0],
                        [0, 1, 0],
                        [0, 1, 0]]
    elif piece == 2:
        piece_matrix = [[0, 2, 2],
                        [2, 2, 0]]
    elif piece == 3:
        piece_matrix = [[3, 0],
                        [3, 3],
                        [0, 3]]
    elif piece == 4:
        piece_matrix = [[0, 4, 0],
                        [4, 4, 4]]
    elif piece == 5:
        piece_matrix = [[5, 0, 0],
                        [5, 5, 5]]
    elif piece == 6:
        piece_matrix = [[6, 6],
                        [6, 6]]
    elif piece == 7:
        piece_matrix = [[7, 7, 0, 0],
                        [0, 7, 7, 0]]
    
    ways = 0
    for i in range(columns - len(piece_matrix[0]) + 1):
        valid_drop = True
        for j in range(len(piece_matrix)):
            for k in range(len(piece_matrix[0])):
                if heights[i + k] + piece_matrix[j][k] > len(heights):
                    valid_drop = False
                    break
            if not valid_drop:
                break
        if valid_drop:
            ways += 1
    
    return ways

# Read input
C, P = map(int, input().split())
heights = list(map(int, input().split()))

# Calculate and print the number of ways
print(tetris_ways(C, P, heights))
```
