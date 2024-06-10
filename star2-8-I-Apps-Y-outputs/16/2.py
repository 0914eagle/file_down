
n = int(input())
a = list(map(int, input().split()))

left = [0] * n
right = [0] * n

for i in range(n):
  left[i] = left[i - 1] + abs(a[i] - a[i - 1])

for i in range(n - 1, -1, -1):
  right[i] = right[i + 1] + abs(a[i] - a[i + 1])

for i in range(n):
  print(left[i] + right[i] - abs(a[i]))

