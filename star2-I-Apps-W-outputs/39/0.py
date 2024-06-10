
def solve(l):
  l = int(l, 2)
  count = 0
  for a in range(l + 1):
    for b in range(l + 1):
      if a + b <= l and a ^ b == a + b:
        count += 1
  return count % (10**9 + 7)

if __name__ == '__main__':
  l = input()
  print(solve(l))

