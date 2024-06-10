
import sys
from collections import Counter
def solve(s):
  n = len(s)
  counter = Counter(s)
  if n < 26:
    return -1
  if n == 26:
    if counter['?'] == 0:
      return s
    else:
      return -1
  i = 0
  while i < n:
    if s[i] == '?':
      c = 'A'
      while c in counter:
        c = chr(ord(c)+1)
      s = s[:i] + c + s[i+1:]
      counter[c] += 1
      i += 1
    else:
      i += 1
  if s.count('?') > 0:
    return -1
  return s
s = sys.stdin.read()
print(solve(s))

