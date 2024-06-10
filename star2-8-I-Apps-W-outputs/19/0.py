
from sys import stdin
from itertools import permutations
s = stdin.readline().strip()
l = len(s)
for p in permutations('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
  ss = list(s)
  for i in range(l):
    if s[i] == '?':
      ss[i] = p[0]
      p = p[1:]
  ss = ''.join(ss)
  for i in range(l):
    if ss[i:i+26] == list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
      print(ss)
      break
  else:
    print(-1)
  break

