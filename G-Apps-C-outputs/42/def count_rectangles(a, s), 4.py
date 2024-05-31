
def count_rectangles(a, s):
    n = len(s)
    s = [int(d) for d in s]
    
    count = 0
    prefix_sums = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sums[i] = prefix_sums[i - 1] + s[i - 1]
    
    total_sum = prefix_sums[n]
    
    for i in range(n):
        for j in range(i, n):
            current_sum = prefix_sums[j + 1] - prefix_sums[i]
            if current_sum == a:
                count += 1
    
    return count

# Input reading
a = int(input())
s = input().strip()

result = count_rectangles(a, s)
print(result)
