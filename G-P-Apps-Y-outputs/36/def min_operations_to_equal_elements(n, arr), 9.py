
def min_operations_to_equal_elements(n, arr):
    operations = []
    
    # Helper function to perform the operation of type 1
    def operation_type_1(i):
        diff = abs(arr[i] - arr[i + 1])
        arr[i] += diff
        operations.append((1, i + 1, i + 2))
    
    # Helper function to perform the operation of type 2
    def operation_type_2(i):
        diff = abs(arr[i] - arr[i + 1])
        arr[i] -= diff
        operations.append((2, i + 1, i + 2))
    
    # Main logic to find the minimum operations
    count = 0
    min_value = min(arr)
    max_value = max(arr)
    
    while min_value != max_value:
        if arr[0] < arr[1]:
            operation_type_1(0)
        else:
            operation_type_2(0)
        
        min_value = min(arr)
        max_value = max(arr)
        count += 1
    
    print(count)
    for op in operations:
        print(*op)

# Input parsing
n = int(input())
arr = list(map(int, input().split()))

# Call the function with the input values
min_operations_to_equal_elements(n, arr)
```
