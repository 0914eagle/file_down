
import sys
n,m = map(int,input().split())
s = [input() for _ in range(n)]
a = [int(e) for e in input().split()]
ans = 0
for i in range(m):
    dic = dict()
    for j in range(n):
        if s[j][i] not in dic:
            dic[s[j][i]] = 1
        else:
            dic[s[j][i]] += 1
    for key,value in dic.items():
        if value > 1:
            ans += a[i] * (value-1)
print(ans)
