
# https://codeforces.com/contest/1295/problem/B

n, r, p = map(int,input().split())

if r < p:
    print(0)
elif p > 2*r:
    print(r)
else:
    print(r + 2*p)
