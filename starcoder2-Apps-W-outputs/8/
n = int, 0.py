
n = int(input())
arr = list(map(int,input().split()))

max_count = 0
max_index = 0

for i in range(n):
    count = 0
    for j in range(n):
        if arr[i] == arr[j]:
            count += 1
    if count > max_count:
        max_count = count
        max_index = i

print(max_index+1,max_index+max_count)
