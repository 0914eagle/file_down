
n = int(input())
p = list(map(int, input().split()))

def lcm(a, b):
  from math import gcd
  return a * b // gcd(a, b)

def modinv(a, m):
  from math import gcd
  if gcd(a, m) != 1:
    return None
  u1, u2, u3 = 1, 0, a
  v1, v2, v3 = 0, 1, m
  while v3 != 0:
    q = u3 // v3
    v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
  return u1 % m

def ncr(n, r, p):
  res = 1
  for i in range(r):
    res = (res * (n - i)) % p
  for i in range(1, r + 1):
    res = (res * modinv(i, p)) % p
  return res

def prob_day(p, n):
  res = 0
  for i in range(n, 0, -1):
    res += (-1)**(n - i) * ncr(n, i, M) * p**i
  return res

M = 998244353
probs = [prob_day(pi / 100, n) for pi in p]
lcm_probs = 1
for prob in probs:
  lcm_probs = lcm(lcm_probs, prob)

def get_day_prob(prob, lcm_probs):
  return prob * modinv(lcm_probs, M) % M

sum_days = 0
for prob in probs:
  day_prob = get_day_prob(prob, lcm_probs)
  sum_days += day_prob * modinv(day_prob, M) % M

print(int(sum_days % M))

