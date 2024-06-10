
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
def binarySearch(arr, target):
  left = 0
  right = len(arr) - 1
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return -1
count = 0
for num in a:
  index = binarySearch(b, num - 1)
  if index != -1:
    count += 1
    b.pop(index)
print(count)

