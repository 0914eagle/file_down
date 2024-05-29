
def count_ways(columns, piece, heights):
    ways = 0
    if piece == 1:
        ways = columns - max(heights)
    elif piece == 2:
        for i in range(len(heights)):
            if i+1 < len(heights) and heights[i] > 0 and heights[i+1] < heights[i]:
                ways += 1
    elif piece == 3:
        for i in range(len(heights)):
            if i+2 < len(heights) and heights[i] > 0 and heights[i+1] < heights[i] and heights[i+2] < heights[i]:
                ways += 1
    elif piece == 4:
        for i in range(len(heights)):
            if i+1 < len(heights) and heights[i] > 0 and heights[i+1] == heights[i]:
                ways += 1
    elif piece == 5:
        for i in range(len(heights)):
            if i+2 < len(heights) and heights[i] > 0 and heights[i+1] < heights[i] and heights[i+2] < heights[i] and (i+3 == len(heights) or heights[i+3] >= heights[i]):
                ways += 1
    elif piece == 6:
        for i in range(len(heights)):
            if i+2 < len(heights) and heights[i] > 0 and heights[i+1] < heights[i] and heights[i+2] < heights[i] and (i+3 == len(heights) or heights[i+3] >= heights[i]):
                ways += 1
            if i+1 < len(heights) and heights[i] > heights[i+1]:
                ways += 1
    elif piece == 7:
        for i in range(len(heights)):
            if i+1 < len(heights) and heights[i] > heights[i+1] and (i+2 == len(heights) or heights[i+2] >= max(heights[i],heights[i+1])):
                ways += 1
    return ways

# Read input
C, P = map(int, input().split())
heights = list(map(int, input().split()))

# Calculate and print output
print(count_ways(C, P, heights))
```

