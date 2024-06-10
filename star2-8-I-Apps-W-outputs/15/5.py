
n = int(input())
a = [int(x) for x in input().split()]

def reorder(arr):
  n = len(arr) // 2
  s1 = sum(arr[:n])
  s2 = sum(arr[n:])

  if s1 == s2:
    return -1

  arr.sort()
  return arr


result = reorder(a)

if result == -1:
  print(-1)
else:
  print(' '.join([str(x) for x in result]))

