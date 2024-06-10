
from itertools import product
def solve(s1, s2):
  s2_list = [c for c in s2]
  for i in range(len(s2_list)):
    if s2_list[i] == '?':
      s2_list[i] = ['+', '-']
  s2_list = sum(s2_list, [])
  result = 0
  for s in s2_list:
    pos = 0
    for c in s:
      if c == '+':
        pos += 1
      else:
        pos -= 1
    if pos == len(s1):
      result += 1
  return result / len(s2_list)

