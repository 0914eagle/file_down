
n, k = map(int, input().split())
h = [int(input()) for i in range(n)]

def check(m):
  cnt = 0
  for hi in h:
    if hi >= m:
      cnt += 1
  return cnt >= k

left = 0
right = 10**9+1
while right - left > 1:
  mid = (left + right) // 2
  if check(mid):
    left = mid
  else:
    right = mid

print(left)

