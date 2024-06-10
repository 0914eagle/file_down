
def solve(n, a, b):
  if b < 2 * a:
    return b * (n // 2) + a * (n % 2)
  else:
    return a * n

q = int(input())
for _ in range(q):
  n, a, b = map(int, input().split())
  print(solve(n, a, b))

