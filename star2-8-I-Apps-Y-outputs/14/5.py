
import math

x = int(input())

def is_perfect_power(n):
    for b in range(1, n + 1):
        for p in range(2, n + 1):
            if pow(b, p) == n:
                return True
    return False

for i in range(x, 0, -1):
    if is_perfect_power(i):
        print(i)
        break

