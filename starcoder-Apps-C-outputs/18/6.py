
from itertools import combinations as C
n, k = map(int, input().split())
l = list(map(int, input().split()))
b = [i for i in range(k+1) if i not in l]
c = [i for i in range(k+1)]
ans = set()
for i in range(1, k+1):
    for j in C(b, i):
        s = sum(j)
        if s in c:
            ans.add(s)
print(len(ans))
print(*sorted(list(ans)))
