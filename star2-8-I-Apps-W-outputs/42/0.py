

def is_d_magic(n, d):
  i = 0
  while n > 0:
    if (i % 2 == 0) and (n % 10 == d):
      return True
    i += 1
    n //= 10
  return False


m, d = map(int, input().split())
a = int(input())
b = int(input())
MOD = 10**9 + 7

res = 0
for n in range(a, b + 1):
  if is_d_magic(n, d) and (n % m == 0):
    res += 1
    res %= MOD

print(res)


