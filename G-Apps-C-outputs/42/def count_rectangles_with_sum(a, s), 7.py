
def count_rectangles_with_sum(a, s):
    n = len(s)
    s = list(map(int, s))
    
    total_rectangles = 0
    
    prefix_sums = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sums[i] = prefix_sums[i - 1] + s[i - 1]
    
    for i in range(n):
        for j in range(i + 1, n):
            current_sum = prefix_sums[j + 1] - prefix_sums[i]
            if current_sum == a:
                total_rectangles += (i + 1) * (n - j)
    
    return total_rectangles

# Input
a = int(input())
s = input().strip()

# Output
print(count_rectangles_with_sum(a, s))
