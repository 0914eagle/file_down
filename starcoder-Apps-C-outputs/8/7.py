
from bisect import bisect_left as bisect
n,m=map(int,input().split())
p=[0]+list(map(int,input().split()))
r=[0]+list(map(int,input().split()))
arr=[]
for i in range(n):
    c,t=map(int,input().split())
    arr.append((c,t))
arr=sorted(arr,key=lambda x:x[1])
ans=0
last=0
for c,t in arr:
    if t>last:
        last=max(last,t)+p[c]
        last-=r[c]
    else:
        last=max(last,t+r[arr[bisect(arr, (c,t))-1][1]])+p[c]
        last-=r[c]
    ans+=1
print(ans)
