
n = int(input())
arr = list(map(int, input().split()))
max_pos = 0
min_pos = 0
for i in range(n):
  if arr[i] == i+1:
    continue
  elif arr[i] > i+1:
    max_pos = i
  else:
    min_pos = i
print(min(max_pos, i-min_pos) + 1)

