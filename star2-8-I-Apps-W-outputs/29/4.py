
import sys
input = sys.stdin.readline
Q = int(input())
update_list = []
def f(x):
  for a, b in update_list:
    x += abs(x - a) + b
  return x
for i in range(Q):
  query = list(map(int, input().split()))
  if query[0] == 1:
    update_list.append([query[1], query[2]])
  else:
    left = -10 ** 9
    right = 10 ** 9
    while left < right:
      mid = (left + right) // 2
      if f(mid) <= f(mid + 1):
        right = mid
      else:
        left = mid + 1
    print(left, f(left))

