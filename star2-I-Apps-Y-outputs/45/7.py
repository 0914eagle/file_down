
def solve(n, a, b):
  if a > 2 * b:
    return n * b
  else:
    return n * a

q = int(input())
for _ in range(q):
  n, a, b = map(int, input().split())
  print(solve(n, a, b))

