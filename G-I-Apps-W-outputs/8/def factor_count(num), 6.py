
from math import isqrt

n = int(input())
arr = list(map(int, input().split()))

def factor_count(num):
    count = 0
    for i in range(1, isqrt(num) + 1):
        if num % i == 0:
            count += 2
        if i * i == num:
            count -= 1
        if count > 7:
            return count
    return count

found = False
for i in range(1, 2**n):
    product = 1
    for j in range(n):
        if i & (1 << j):
            product *= arr[j]
    
    if isqrt(product)**2 == product:
        found = True
        print(bin(i).count('1'))
        break

if not found:
    print(-1)
```
