
n,m = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
for i in range(m):
    l,r = map(int,input().split())
    ans += sum(a[l-1:r])
print(ans)
