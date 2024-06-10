
import math

def gcd(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    return math.gcd(numbers[0], gcd(numbers[1:]))

n = int(input())
numbers = list(map(int, input().split()))

numbers = list(set(numbers)) # remove duplicates
numbers.sort()

max_group_size = 0
for i in range(len(numbers)):
  for j in range(i+1, len(numbers)+1):
    if gcd(numbers[i:j]) == 1:
      max_group_size = max(max_group_size, j-i)

print(max_group_size)

