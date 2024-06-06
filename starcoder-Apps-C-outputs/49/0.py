
from collections import Counter
x, a, b = input().split()
x = int(x)
a = int(a)
b = int(b)
n = list(input())
counter = Counter(n)
if len(n) == 1:
    t = (b - a)//x + 1
    print(t)
else:
    ans = 0
    for i in range(a, b+1, x):
        if all([n[0] in str(i), n[1] in str(i)]):
            ans += 1
    print(ans)
