
n = int(input())
a = [int(i) for i in input().split()]

left = [0] * n
right = [0] * n
count = [0] * (max(a) + 1)

for i in range(n):
  count[a[i]] += 1
  left[i] = count[a[i]] - 1

count = [0] * (max(a) + 1)
for i in range(n - 1, -1, -1):
  count[a[i]] += 1
  right[i] = count[a[i]] - 1

ans = 0
for i in range(n - 1):
  if left[i] > right[i + 1]:
    ans += 1

print(ans)

