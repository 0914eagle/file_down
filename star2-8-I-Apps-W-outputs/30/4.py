
def bubble_sort(arr):
    swaps = []
    
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps.append((j, j+1))
    
    return swaps
n = int(input())
arr = list(map(int, input().split()))

swaps = bubble_sort(arr)
print(len(swaps))
for i, j in swaps:
    print(i, j)

