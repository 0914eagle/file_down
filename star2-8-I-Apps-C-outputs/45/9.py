
from math import gcd

n = int(input())
s = [int(i) for i in input().split()]

count = 1 # The first pokemon
for i in range(1, n):
  can_take = True
  for j in range(i):
    if gcd(s[i], s[j]) != 1:
      can_take = False
      break
  if can_take:
    count += 1
    
print(count)

