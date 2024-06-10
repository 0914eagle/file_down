
def solve(n, m, p, seq, ops):
  stack = []
  for op in ops:
    if op == "L":
      p -= 1
      if p < 1:
        p = 1
    elif op == "R":
      p += 1
      if p > n:
        p = n
    elif op == "D":
      stack = []
      for i in range(1, p):
        stack.append(seq[i-1])
      for i in range(p+1, n+1):
        stack.append(seq[i-1])
      seq = "".join(stack)
      n = len(seq)
      p -= 1
      if p < 1:
        p = 1
  return seq

n, m, p = map(int, input().split())
seq = input()
ops = input()
print(solve(n, m, p, seq, ops))

