
def count_rectangles(a, s):
    n = len(s)
    total_count = 0

    prefix_sum = [0]
    for i in range(n):
        prefix_sum.append(prefix_sum[-1] + int(s[i]))

    for i in range(n):
        for j in range(i+1, n):
            current_sum = prefix_sum[j+1] - prefix_sum[i]
            if current_sum == a:
                total_count += (i+1) * (n-j)

    return total_count

# Input
a = int(input())
s = input()

# Output
print(count_rectangles(a, s))
