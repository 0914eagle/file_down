
n = int(input())
arr = list(map(int, input().split()))

max_count = 0
max_num = 0

for i in range(n):
    count = 0
    for j in range(n):
        if arr[i] == arr[j]:
            count += 1
    if count > max_count:
        max_count = count
        max_num = arr[i]

l = 0
r = 0

for i in range(n):
    if arr[i] == max_num:
        l = i
        break

for i in range(n-1, -1, -1):
    if arr[i] == max_num:
        r = i
        break

print(l+1, r+1)
