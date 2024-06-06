
# 354
N = int(input())
a = list(map(int, input().split()))

for i in range(N):
  if a[i-1] > a[i]:
    print(i, i+1)
    a[i] += a[i-1]

if a[-2] > a[-1]:
  print(N, N)
  a[-1] += a[-2]

