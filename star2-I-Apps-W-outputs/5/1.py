
def solve(n, r):
    max_len = 0
    sum_r = 0
    left = 0
    for right in range(n):
        sum_r += r[right]
        while sum_r > 100:
            sum_r -= r[left]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
n = int(input())
r = list(map(int, input().split()))
print(solve(n, r))

