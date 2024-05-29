
def count_ways(C, P, heights):
    piece_shapes = [
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (0, 1), (1, 0), (1, 1)],
        [(0, 0), (0, 1), (0, 2), (1, 1)],
        [(0, 0), (0, 1), (0, 2), (1, 0)],
        [(0, 0), (0, 1), (0, 2), (1, 2)],
        [(0, 0), (1, 0), (1, 1), (1, 2)],
        [(0, 0), (0, 1), (0, 2), (1, 2)]
    ]
    
    ways = 0
    for shift in range(max(heights) - 4 + 1):
        for col in range(C):
            valid = True
            for square in piece_shapes[P-1]:
                row = square[0] + shift + heights[col] - 1
                new_col = square[1] + col
                if row >= 0 and new_col < C and new_col >= 0:
                    if heights[new_col] - heights[col] < row - heights[col]:
                        valid = False
                        break
                else:
                    valid = False
                    break
            if valid:
                ways += 1
    
    return ways

# Read input
C, P = map(int, input().split())
heights = list(map(int, input().split()))

# Calculate and print the number of ways
print(count_ways(C, P, heights))
```
