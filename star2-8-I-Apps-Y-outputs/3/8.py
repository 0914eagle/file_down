
n, l = map(int, input().split())

def solve(n, l):
  if n == 1:
    return 0
  else:
    return l + n - 1 + solve(n-1, l+1)

print(solve(n, l))

