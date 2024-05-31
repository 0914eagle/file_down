
def count_rectangles_with_sum(s, a):
    n = len(s)
    s = list(map(int, s))

    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + s[i - 1]

    count = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            current_sum = prefix_sum[j] - prefix_sum[i - 1]
            if current_sum == a:
                count += 1

    return count

# Input
a = int(input())
s = input().strip()

# Output
print(count_rectangles_with_sum(s, a))
