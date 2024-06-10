
n = int(input())
a = list(map(int, input().split()))

freq = [0 for i in range(10**6 + 1)]
for x in a:
  freq[x] += 1

sum_first_half = sum(a[:n])
sum_last_half = sum(a[n:])
for x in range(10**6, -1, -1):
  if freq[x] > 0:
    if freq[x] <= sum_first_half:
      freq[x] = 0
      sum_first_half -= x
    else:
      freq[x] -= sum_first_half
      sum_first_half = 0
    if freq[x] <= sum_last_half:
      freq[x] = 0
      sum_last_half -= x
    else:
      freq[x] -= sum_last_half
      sum_last_half = 0
  if sum_first_half == 0 and sum_last_half == 0:
    break

if sum_first_half != sum_last_half:
  print(-1)
else:
  res = []
  for x in range(10**6, -1, -1):
    res += [x] * freq[x]
  print(*res)

