
from itertools import product

def solve(s1, s2):
  if len(s1) != len(s2):
    return 0
  possible_s2 = []
  for s in product(['+', '-'], repeat=s2.count('?')):
    possible_s2.append(''.join(s))
  total = len(possible_s2)
  correct = 0
  for s in possible_s2:
    if all([a == b for a, b in zip(s1, s)]):
      correct += 1
  return correct / total

