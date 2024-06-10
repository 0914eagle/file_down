
from sys import stdin
from collections import defaultdict

def read_ints():
  return list(map(int, stdin.readline().strip().split()))

def solve(hotdogs, buns):
  n = len(hotdogs)
  m = len(buns)

  dp = defaultdict(lambda: float('inf'))
  dp[0] = 0

  for i in range(n):
    for j in range(m):
      for k in range(1001):
        if k - hotdogs[i] - buns[j] >= 0:
          dp[k] = min(dp[k], dp[k - hotdogs[i] - buns[j]] + 1)

  for k in range(1, 1001):
    if dp[k] < float('inf'):
      return k

  return "impossible"

def main():
  hotdogs = read_ints()[1:]
  buns = read_ints()[1:]

  print(solve(hotdogs, buns))

if __name__ == "__main__":
  main()

