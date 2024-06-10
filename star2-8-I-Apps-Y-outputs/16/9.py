
n = int(input())
a = list(map(int, input().split()))

left = [0] * n
right = [0] * n

left[0] = a[0]
right[-1] = a[-1]

for i in range(1, n):
  left[i] = left[i-1] + a[i]
  right[n-i-1] = right[n-i] + a[n-i-1]

for i in range(n):
  print(abs(left[i-1] - right[i]) + abs(left[i] - right[i]) + abs(left[i+1] - right[i]))


