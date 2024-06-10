
n, p, k = map(int, input().split())
t = list(map(int, input().split()))
def calc_time(n, p, k, t):
  time = 0
  for i in range(n):
    time += (t[i] - time) * (100 + i * p) / 100
  time += (k - t[-1]) * (100 + n * p) / 100
  return time
left = 0
right = k
while right - left > 1e-6:
  mid = (left + right) / 2
  if calc_time(n, p, mid, t) > k:
    right = mid
  else:
    left = mid
print(left)

