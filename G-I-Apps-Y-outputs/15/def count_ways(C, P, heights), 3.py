
def count_ways(C, P, heights):
    piece_configurations = [
        [(0, 0), (0, 1), (0, 2), (1, 1)],  # Piece 1
        [(0, 0), (0, 1), (0, 2), (0, 3)],  # Piece 2
        [(0, 0), (0, 1), (1, 1), (1, 2)],  # Piece 3
        [(0, 0), (0, 1), (1, 0), (1, 1)],  # Piece 4
        [(0, 0), (0, 1), (1, 1), (1, 2)],  # Piece 5
        [(0, 0), (0, 1), (0, 2), (1, 0)],  # Piece 6
        [(0, 0), (0, 1), (0, 2), (1, 2)]   # Piece 7
    ]
    
    ways = 0
    for config in piece_configurations[P-1]:
        piece_heights = [heights[i] for i in range(config[1] - config[0] + 1)]
        min_height = min(piece_heights)
        for col in range(C - config[1] + config[0] + 1):
            valid_drop = True
            for i in range(config[1] - config[0] + 1):
                if heights[col + i] - heights[col + i - config[0]] > piece_heights[i] - min_height:
                    valid_drop = False
                    break
            if valid_drop:
                ways += 1
    
    return ways

# Input
C, P = map(int, input().split())
heights = list(map(int, input().split()))

# Output
print(count_ways(C, P, heights))
```
