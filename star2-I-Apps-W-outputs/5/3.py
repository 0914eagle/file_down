
def ddos(n, r):
    left = 0
    right = 0
    max_len = 0
    sum_r = 0
    while right < n:
        if sum_r + r[right] <= 100:
            sum_r += r[right]
            right += 1
        else:
            sum_r -= r[left]
            left += 1
        max_len = max(max_len, right - left)
    return max_len

n = int(input())
r = list(map(int, input().split()))
print(ddos(n, r))

