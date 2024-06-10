
from collections import defaultdict

def solve(N, K, marbles):
  counts = defaultdict(int)
  max_count = 0
  for marble in marbles:
    counts[marble] += 1
    max_count = max(max_count, counts[marble])
  return K - max_count

N, K = map(int, input().split())
marbles = list(map(int, input().split()))
print(solve(N, K, marbles))

