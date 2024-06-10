
def solve(n, l, r):
  min_sum = 0
  max_sum = 0
  for i in range(l):
    min_sum += 1
    max_sum += 1
  for i in range(l, r):
    min_sum += 2
    max_sum += 2 ** (i - l + 1)
  return min_sum, max_sum

n, l, r = map(int, input().split())
min_sum, max_sum = solve(n, l, r)
print(min_sum, max_sum)

