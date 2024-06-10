
n = int(input())
p = [int(x) for x in input().split()]

def findIndex(arr, item):
  for i in range(len(arr)):
    if arr[i] == item:
      return i
  return -1

def countSwaps(arr):
  count = 0
  for i in range(n):
    pos = findIndex(arr, i+1)
    if pos != i:
      arr[i], arr[pos] = arr[pos], arr[i]
      count += 1
  return count

print(countSwaps(p))

