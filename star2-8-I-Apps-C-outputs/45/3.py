
from math import gcd

n = int(input())
s = list(map(int, input().split()))

count = 0
for i in range(n):
    flag = 0
    for j in range(i):
        if gcd(s[i], s[j]) != 1:
            flag = 1
            break
    if not flag:
        count += 1
print(count)

