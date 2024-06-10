
n, k = map(int, input().split())
for x in range(n+1, 10**10):
  if x % k == 0:
    print(x)
    break

