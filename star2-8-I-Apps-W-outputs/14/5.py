
def solve(n):
  unfairness = 0
  n_bin = bin(n)[2:]
  for i in range(len(n_bin) - 1):
    if n_bin[i] != n_bin[i+1]:
      unfairness += 2 ** (len(n_bin) - i - 1)
  return unfairness

t = int(input())
for i in range(t):
  n = int(input())
  print(solve(n))

