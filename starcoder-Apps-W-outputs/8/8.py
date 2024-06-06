
from itertools import combinations
n,m,k = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
arr.reverse()
ans = []
for i in range(k):
    ans.append(sum(arr[m*i:m*(i+1)]))
print(sum(ans))
print(" ".join(map(str,range(m,m*(k-1)+1,m))))
