
def solve(n, a, b):
  if b < 2 * a:
    return n * a
  else:
    return n * b // 2

q = int(input())
for _ in range(q):
  n, a, b = map(int, input().split())
  print(solve(n, a, b))

