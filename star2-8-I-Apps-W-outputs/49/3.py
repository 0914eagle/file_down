
def solve(n, k, h):
  res = 1
  for i in range(n):
    res = res * k % 998244353
  return res

if __name__ == '__main__':
  n, k = map(int, input().split())
  h = list(map(int, input().split()))
  print(solve(n, k, h))

