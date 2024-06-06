
# python 3

import itertools
import functools

def partition(lst, n):
    division = itertools.combinations(range(1,len(lst)), n-1)
    return [(lst[i:j], lst[j:]) for i,j in division]

n, m, k = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

ans = []

for p in itertools.combinations(range(1, len(arr)), k - 1):
    ans.append(p)

idx = 0

for p in ans:
    p = list(p)
    p.insert(0, 0)
    p.append(len(arr))
    print(p)
    arr_ = []
    for i in range(1, len(p)):
        arr_.append(arr[p[i - 1]:p[i]])
    print(arr_)
