
from math import factorial
n = int(input())
e = 0
for i in range(n + 1):
e += 1 / factorial(i)
print(e)

