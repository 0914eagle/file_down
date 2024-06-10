
from collections import defaultdict

s = input()
q = int(input())
freq = defaultdict(int)

for _ in range(q):
  query = input().split()
  if query[0] == "1":
    pos = int(query[1])
    c = query[2]
    freq[s[pos-1]] -= 1
    s = s[:pos-1] + c + s[pos:]
    freq[s[pos-1]] += 1
  elif query[0] == "2":
    l = int(query[1])
    r = int(query[2])
    print(len(set(s[l-1:r])))


