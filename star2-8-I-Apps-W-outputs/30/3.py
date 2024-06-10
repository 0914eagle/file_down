
n = int(input())
arr = list(map(int, input().split()))
def min_index(arr, i):
    idx = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[idx]:
            idx = j
    return idx

def sort_arr(arr):
    res = []
    for i in range(len(arr)-1):
        idx = min_index(arr, i)
        if idx != i:
            res.append([i, idx])
            temp = arr[i]
            arr[i] = arr[idx]
            arr[idx] = temp
    return res
res = sort_arr(arr)
print(len(res))
for r in res:
    print(r[0], r[1])

