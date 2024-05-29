
import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def is_sequence_in_table(n, m, k, a):
    for i in range(1, k + 1):
        if gcd(n, i) != a[i - 1]:
            return "NO"
    return "YES"

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(is_sequence_in_table(n, m, k, a))
```
