
# bisect_left
# by 
# O(nlogn) time for N queries, O(n) space

def bisect_left(a, x, lo=0, hi=None):
    

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x > a[mid]: lo = mid+1
        else: hi = mid
    return lo

n, k = [int(x) for x in input().split()]

A = []
B = []

for _ in range(n):
    a = [int(x) for x in input().split()]
    A.append(a)
    b = a.count(1)
    B.append(b)

B.sort()

for i in range(n):
    if (i - bisect_left(B, k//2)) > k//2:
        print("NO")
        break
else:
    print("YES")

