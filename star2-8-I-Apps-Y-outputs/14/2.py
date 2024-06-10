
from math import sqrt

def is_perfect_power(n):
    for b in range(1, int(sqrt(n)) + 1):
        for p in range(2, n + 1):
            if b**p == n:
                return True
    return False

x = int(input())
for n in range(x, 0, -1):
    if is_perfect_power(n):
        print(n)
        break

