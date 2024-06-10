
n = int(input())
a = list(map(int, input().split()))

a.sort()

ans = 360
for i in range(n):
    s1 = sum(a[:i])
    s2 = sum(a[i:])
    ans = min(ans, abs(s1 - s2))

print(ans)

