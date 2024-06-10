
n = int(input())
arr = [int(i) for i in input().split()]
count = 0
for i in range(n):
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            print(i, j)
            count += 1
    if count == n:
        break

