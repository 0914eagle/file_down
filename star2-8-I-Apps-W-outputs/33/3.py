

from itertools import product

def solve(s1, s2):
  n = len(s1)
  pos = [0] * n
  unrecognized = []
  for i in range(n):
    if s2[i] == '?':
      unrecognized.append(i)
    else:
      pos[i] = 1 if s2[i] == '+' else -1
  res = 0
  for p in product([1, -1], repeat=len(unrecognized)):
    for i in range(len(unrecognized)):
      pos[unrecognized[i]] = p[i]
    if sum(pos) == 0:
      res += 1
  return res / (2 ** len(unrecognized))


def main():
  s1 = input()
  s2 = input()
  print(solve(s1, s2))


if __name__ == '__main__':
  main()


