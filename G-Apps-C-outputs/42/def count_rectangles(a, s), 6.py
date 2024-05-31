
def count_rectangles(a, s):
    n = len(s)
    count = 0
    for x in range(1, n+1):
        for y in range(x, n+1):
            prefix_sum = [0] * (n+1)
            for i in range(1, n+1):
                prefix_sum[i] = int(s[i-1]) + prefix_sum[i-1]
            for z in range(1, n+1):
                for t in range(z, n+1):
                    sum_rect = prefix_sum[y] - prefix_sum[x-1]
                    sum_rect *= (prefix_sum[t] - prefix_sum[z-1])
                    if sum_rect == a:
                        count += 1
    return count

# Input
a = int(input())
s = input().strip()

# Output
print(count_rectangles(a, s))
