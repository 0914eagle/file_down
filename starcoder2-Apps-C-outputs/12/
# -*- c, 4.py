
# -*- coding: utf-8 -*-


n,a,b,k = map(int,input().split())
s = input()

s = s*int(n/k+1)

ans = 0

for i in range(n+1):
    if s[i] == '+':
        ans += a**(n-i)*b**i
    else:
        ans -= a**(n-i)*b**i

print(ans%(10**9+9))
