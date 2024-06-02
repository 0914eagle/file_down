
def sum_of_values(n, rectangles):
    table = [[0] * 100 for _ in range(100)]
    
    for rect in rectangles:
        x1, y1, x2, y2 = rect
        for i in range(y1-1, y2):
            for j in range(x1-1, x2):
                table[i][j] += 1
    
    total_sum = sum(sum(row) for row in table)
    return total_sum

# Read input
n = int(input())
rectangles = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    rectangles.append((x1, y1, x2, y2))

# Calculate and print the result
result = sum_of_values(n, rectangles)
print(result)