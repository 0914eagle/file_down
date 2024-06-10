
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.sort()

def f(l, r):
  return sum(a[i] * b[i] for i in range(l, r+1))

ans = 0
for l in range(n):
  for r in range(l, n):
    ans += f(l, r)

print(ans % 998244353)

