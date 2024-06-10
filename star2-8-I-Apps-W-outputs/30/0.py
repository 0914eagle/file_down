
n = int(input())
arr = [int(x) for x in input().split()]

def find_min(arr):
    min_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
    return min_idx

def find_max(arr):
    max_idx = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[max_idx]:
            max_idx = i
    return max_idx

def swap_min_max(arr):
    min_idx = find_min(arr)
    max_idx = find_max(arr)
    
    temp = arr[min_idx]
    arr[min_idx] = arr[max_idx]
    arr[max_idx] = temp
    
    return arr

def sort_in_n_swaps(arr):
    sorted_arr = []
    
    for _ in range(len(arr)):
        arr = swap_min_max(arr)
        sorted_arr.append(arr.pop())
        
    return sorted_arr

sorted_arr = sort_in_n_swaps(arr)

print(len(arr))
for i in range(len(arr)):
    print(f'{i} {len(arr) - i - 1}')

