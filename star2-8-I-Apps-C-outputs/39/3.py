
import bisect

def solve(lst):
  pairs = dict()
  for i, x in enumerate(lst):
    for j, y in enumerate(lst):
      if i != j:
        pairs[x + y] = pairs.get(x + y, []) + [(i, j)]
  lst.sort()
  res = 0
  for x in lst:
    idx = bisect.bisect_left(lst, -x)
    res += len(pairs.get(-x, [])) + len(pairs.get(x, []))
  return res // 3

