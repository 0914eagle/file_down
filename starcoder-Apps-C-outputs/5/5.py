
n = int(input())
a = list(map(int,input().split()))
res = 0
for i in range(1,n-1):
    res += min(a[i-1],a[i+1])
print(res)
