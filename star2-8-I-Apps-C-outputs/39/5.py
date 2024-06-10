
n = int(input())
a = list(map(int, input().split()))
a.sort()

left = 0
right = len(a) - 1

count = 0
while left < right:
  if a[left] + a[right] in a[left + 1 : right]:
    count += 1
  if -a[left] - a[right] in a[left + 1 : right]:
    count += 1
  if a[left] + a[right] < 0:
    left += 1
  else:
    right -= 1

print(count)

