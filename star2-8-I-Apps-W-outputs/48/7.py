
def solve(k):
  i = 1
  cnt = 0
  while True:
    if sum(map(int, str(i))) == 10:
      cnt += 1
      if cnt == k:
        return i
    i += 1

k = int(input())
print(solve(k))

