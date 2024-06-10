
def max_chests(chests, keys):
  chests.sort()
  keys.sort()
  total = 0
  i = 0
  for key in keys:
    while i < len(chests) and (chests[i] + key) % 2 != 1:
      i += 1
    if i < len(chests):
      total += 1
      i += 1
  return total

n, m = map(int, input().split())
chests = list(map(int, input().split()))
keys = list(map(int, input().split()))
print(max_chests(chests, keys))

