
n,d,m = map(int,input().split())
a = [int(input()) for i in range(m)]
a.sort()
l = 0
ans = 0
for i in range(m):
    ans += max(0,a[i] - l - d - 1)
    l = max(l,a[i] + d + 1)
ans += max(0,n - d - l - 1)
print(ans)
