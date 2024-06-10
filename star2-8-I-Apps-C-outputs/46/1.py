
import sys

def gcd(a, b):
  if a == 0:
    return b
  return gcd(b % a, a)

def lcm(a, b):
  return a * b // gcd(a, b)

def chinese_remainder_theorem(n, a):
  product = 1
  for i in n:
    product *= i

  result = 0
  for i in range(len(n)):
    p = product // n[i]
    result += a[i] * mul_inv(p, n[i]) * p

  return result % product

def mul_inv(a, b):
  b0 = b
  x0, x1 = 0, 1
  if b == 1:
    return 1
  while a > 1:
    q = a // b
    a, b = b, a % b
    x0, x1 = x1 - q * x0, x0
  if x1 < 0:
    x1 += b0
  return x1

m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
n = [m[i] + 2 * y[i] + 1 for i in range(len(m))]
a = [x[i] + y[i] + 1 for i in range(len(m))]
print(chinese_remainder_theorem(n, a))

