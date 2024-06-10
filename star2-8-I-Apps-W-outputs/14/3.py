
import math

def unfairness(n):
  return (n+1)*n//2 - math.floor(n/2) - math.ceil(n/2)

t = int(input())
for i in range(t):
  n = int(input())
  print(unfairness(n))

