
from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

n, m = map(int, input().split())

a = list(map(int, input().split()))

a.sort()

a = list(powerset(a))

for k in a:
    for i in range(n):
        if len(k) == i:
            print(i)
            print(*k)
            exit()
