
from collections import defaultdict

def build_road(n, a):
  districts_by_gang = defaultdict(set)
  for i, gang in enumerate(a, 1):
    districts_by_gang[gang].add(i)

  roads = []
  for gang, districts in districts_by_gang.items():
    if len(districts) > 1:
      districts = sorted(districts)
      for i in range(1, len(districts)):
        roads.append((districts[i-1], districts[i]))

  if len(roads) == n-1:
    return "YES\n" + "\n".join(f"{x} {y}" for x, y in roads)
  else:
    return "NO"

t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))
  print(build_road(n, a))

