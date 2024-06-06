
# Solution 1:
import random

n, d, c = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

s1 = 0
s2 = 0

res = 0

for i in range(n):
    s1 += (1 if i in A else 0)
    s2 += (1 if i in B else 0)

for i in range(100000):
    x = random.choices(range(1, n+1), k=d)
    p1 = 0
    p2 = 0

    for i in range(d):
        p1 += (1 if x[i] in A else 0)
        p2 += (1 if x[i] in B else 0)
    if p1 == c or p2 == c:
        res += 1

print(res / 100000)
