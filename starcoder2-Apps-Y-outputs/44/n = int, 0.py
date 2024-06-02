
n = int(input())
a = list(map(int, input().split()))

l = 0
r = n - 1
ans = 0

while l <= r:
    if l == r:
        ans = max(ans, 1)
        break
    if a[r] <= a[l] * 2:
        ans = max(ans, r - l + 1)
        r -= 1
    else:
        l += 1

print(ans)

