
n,m = map(int,input().split())

a = list(map(int,input().split()))

res = 0
for i in range(n):
    res += (m - a[i])//2
    
print(res)
