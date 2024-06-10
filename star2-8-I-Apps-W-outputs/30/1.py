
n = int(input())
arr = list(map(int, input().split()))

swaps = []

for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    
    if min_idx != i:
        swaps.append((i, min_idx))
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(len(swaps))
for i, j in swaps:
    print(i, j)


