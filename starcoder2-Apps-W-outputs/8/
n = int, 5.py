
n = int(input())
arr = list(map(int, input().split()))

max_count = 0
max_count_index = 0

for i in range(n):
    count = arr.count(arr[i])
    if count > max_count:
        max_count = count
        max_count_index = i

print(max_count_index + 1, max_count_index + max_count)
