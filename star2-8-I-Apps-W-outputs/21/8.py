
import math

MOD = 998244353

def inverse(a):
  return pow(a, MOD - 2, MOD)

n = int(input())
ps = [int(x) for x in input().split()]

probs = [p / 100 for p in ps]

def calc_expected_days(probs):
  n = len(probs)
  probs_prod = [1.0]
  for i in range(n):
    probs_prod.append(probs_prod[-1] * probs[i])
  p_sum = 0.0
  for i in range(n):
    p_sum += probs_prod[i] * probs_prod[n - i] * (n - i)
  return 1.0 / p_sum

expected_days = calc_expected_days(probs)

def calc_expected_days_mod(expected_days):
  num = int(expected_days * MOD)
  den = int(expected_days)
  return (num * inverse(den)) % MOD

print(calc_expected_days_mod(expected_days))

