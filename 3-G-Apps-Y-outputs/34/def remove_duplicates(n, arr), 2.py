
def remove_duplicates(n, arr):
    unique_elements = {}
    for i in range(n-1, -1, -1):
        if arr[i] not in unique_elements:
            unique_elements[arr[i]] = i
    
    result = list(unique_elements.keys())
    result.sort(key=lambda x: unique_elements[x])
    
    return len(result), result

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
num_elements, unique_arr = remove_duplicates(n, arr)
print(num_elements)
print(' '.join(map(str, unique_arr)))
