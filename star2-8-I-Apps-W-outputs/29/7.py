
from sys import stdin
readline = stdin.readline
def update(a, b):
  for i in range(a, n+1):
    f[i] += i - a + b
def evaluate():
  m = 10**9
  x = 0
  for i in range(n+1):
    if f[i] < m:
      m = f[i]
      x = i
  return x, m
n = 2*10**5
f = [0]*(n+1)
q = int(readline())
for _ in range(q):
  t, *ab = map(int, readline().split())
  if t == 1:
    a, b = ab
    update(a, b)
  else:
    x, m = evaluate()
    print(x, m)

