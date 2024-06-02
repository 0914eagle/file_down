
def calculate_sum_of_values(n, rectangles):
    table = [[0 for _ in range(101)] for _ in range(101)]
    
    for rect in rectangles:
        x1, y1, x2, y2 = rect
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                table[i][j] += 1
    
    total_sum = sum(sum(row) for row in table)
    return total_sum

# Input processing
n = int(input())
rectangles = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    rectangles.append((x1, y1, x2, y2))

result = calculate_sum_of_values(n, rectangles)
print(result)
