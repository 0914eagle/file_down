
n = int(input())
arr = list(map(int, input().split()))
idx = {val: i for i, val in enumerate(arr)}

def find_next_larger(arr, idx, start):
    next_larger = None
    for i in range(start, len(arr)):
        if arr[i] > arr[start] and (next_larger is None or arr[i] < arr[next_larger]):
            next_larger = i
    return next_larger

swaps = []
for i in range(len(arr)):
    next_larger = find_next_larger(arr, idx, i)
    if next_larger is None:
        continue
    
    swaps.append((i, next_larger))
    arr[i], arr[next_larger] = arr[next_larger], arr[i]
    idx[arr[i]] = i
    idx[arr[next_larger]] = next_larger

print(len(swaps))
for swap in swaps:
    print(swap[0], swap[1])

