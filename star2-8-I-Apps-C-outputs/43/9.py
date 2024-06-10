
from sys import stdin
input = stdin.readline
n = int(input())
s = input().rstrip()

def solve(s):
  zero_one = s.count('0')
  one_zero = s.count('1')

  return max(zero_one, one_zero) + 1

print(solve(s))

