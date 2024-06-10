
import math

n = int(input())

if n == 0 or n == 1:
    print(0)
else:
    print(math.factorial(n) // (2 * math.factorial(n - 2)))

