
from itertools import combinations
s = input()
n = len(s)
ans = 0
for i in range(1,n+1):
    for j in combinations(range(n),i):
        if all(j[k+1]-j[k]==j[1]-j[0] for k in range(i-1)):
            ans += 1
print(ans)
