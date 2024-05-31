
def count_rectangles(a, s):
    total_rectangles = 0
    n = len(s)
    prefix_sum = [0] * (n + 1)
    
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + int(s[i - 1])
    
    for x in range(n):
        for y in range(x, n):
            current_sum = prefix_sum[y + 1] - prefix_sum[x]
            if current_sum == a:
                total_rectangles += 1
    
    return total_rectangles

# Input
a = int(input())
s = input().strip()

# Output
print(count_rectangles(a, s))
