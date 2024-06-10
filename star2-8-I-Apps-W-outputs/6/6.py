
from functools import reduce

def mod_inv(x, mod):
  return pow(x, mod-2, mod)

def factorial(n, mod):
  return reduce(lambda x, y: x*y % mod, range(1, n+1), 1)

def binom(n, k, mod):
  return factorial(n, mod) * mod_inv(factorial(k, mod), mod) % mod * mod_inv(factorial(n-k, mod), mod) % mod

def count_probs(n, m, probs):
  probs = [prob for prob in probs if prob != 0]
  prob_sum = len(probs)
  if prob_sum == 0:
    return 0
  probs = [prob for prob in probs if prob != m+1]
  prob_sum = len(probs)
  if prob_sum == 0:
    return 0
  prob_sum = sum(probs)
  return binom(prob_sum-1, n-1, 10**9+7)

def solve(s1, s2):
  probs1 = [s1[i]+1 for i in range(len(s1)) if s1[i] == 0]
  probs2 = [s2[i]+1 for i in range(len(s2)) if s2[i] == 0]
  prob1 = count_probs(len(s1), len(probs1), probs1)
  prob2 = count_probs(len(s2), len(probs2), probs2)
  return (prob1-prob2) % (10**9+7)

def main():
  n, m = [int(x) for x in input().split()]
  s1 = [int(x) for x in input().split()]
  s2 = [int(x) for x in input().split()]
  print(solve(s1, s2))

if __name__ == "__main__":
  main()

