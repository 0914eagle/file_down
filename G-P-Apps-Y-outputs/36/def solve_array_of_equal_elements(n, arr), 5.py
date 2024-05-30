
def solve_array_of_equal_elements(n, arr):
    operations = []
    min_operations = 0
    
    # Find the minimum element in the array
    min_elem = min(arr)
    
    # Find the maximum difference from the minimum element in the array
    max_diff = max([abs(elem - min_elem) for elem in arr])
    
    while max_diff > 0:
        for i in range(n-1):
            if arr[i] != arr[i+1]:
                if abs(arr[i]-arr[i+1]) == max_diff:
                    min_operations += 1
                    if arr[i] > arr[i+1]:
                        operations.append((2, i+1, i))
                        arr[i] -= max_diff
                    else:
                        operations.append((1, i+1, i))
                        arr[i] += max_diff
                    break
        max_diff = max([abs(elem - min(arr)) for elem in arr])
    
    print(min_operations)
    for op in operations:
        print(" ".join(map(str, op)))

# Input reading and function call
n = int(input())
arr = list(map(int, input().split()))
solve_array_of_equal_elements(n, arr)
```
