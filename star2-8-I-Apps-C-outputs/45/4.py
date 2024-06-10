
from math import gcd
n = int(input())
s = list(map(int, input().split()))

lcm = 1
for i in s:
    lcm = lcm * i // gcd(lcm, i)
count = 0
for i in s:
    if gcd(lcm, i) > 1:
        count += 1
print(n - count)


