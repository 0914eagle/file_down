
def solve(n, l):
  flavor = []
  for i in range(n):
    flavor.append(l + i)
  min_diff = 10**9
  for i in range(n):
    remaining_flavor = []
    for j in range(n):
      if j == i:
        continue
      remaining_flavor.append(flavor[j])
    remaining_flavor_sum = sum(remaining_flavor)
    diff = abs(remaining_flavor_sum - flavor[i])
    if diff < min_diff:
      min_diff = diff
  return flavor[i] - min_diff

n, l = map(int, input().split())
print(solve(n, l))

