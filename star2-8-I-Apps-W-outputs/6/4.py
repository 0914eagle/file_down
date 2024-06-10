
from collections import Counter
n, m = map(int, input().split())
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))

zero1 = s1.count(0)
zero2 = s2.count(0)

if zero1 + zero2 == n:
    print(0)

elif zero1 == 0 or zero2 == 0:
    print(0 if zero1 == 0 else 1)

else:
    c1 = Counter(s1)
    c2 = Counter(s2)
    p = 1
    for i in range(1, m+1):
        p = (p * (c1[i] + 1) * (c2[i] + 1)) % (10**9+7)
    q = (zero1 + 1) * (zero2 + 1)
    qinv = pow(q, 10**9+5, 10**9+7)
    print(p*qinv % (10**9+7))

