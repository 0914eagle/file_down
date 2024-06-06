
def get_min_dist(arr,d):
  arr.sort()
  n = len(arr)
  mid = n//2
  sum_val = 0
  for i in range(n):
    sum_val += abs(arr[i] - arr[mid])
  if sum_val <= d:
    return sum_val
  elif arr[mid] < arr[mid-1]:
    if abs(arr[mid]-arr[mid-1]) > d:
      return arr[mid]
    return abs(arr[mid]-arr[mid-1])
  else:
    if abs(arr[mid]-arr[mid+1]) > d:
      return arr[mid]
    return abs(arr[mid]-arr[mid+1])

n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
d = int(input())

min_x = get_min_dist(x,d)
min_y = get_min_dist(y,d)

print(min_x + min_y)
