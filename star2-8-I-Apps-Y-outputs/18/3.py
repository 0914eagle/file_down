
import math
n = int(input())
approximation = 0
for i in range(n+1):
approximation += 1/math.factorial(i)
print(approximation)

