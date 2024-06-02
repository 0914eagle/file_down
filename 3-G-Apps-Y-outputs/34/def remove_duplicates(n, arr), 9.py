
def remove_duplicates(n, arr):
    unique_elements = []
    element_positions = {}
    
    for i in range(n-1, -1, -1):
        if arr[i] not in element_positions:
            unique_elements.append(arr[i])
            element_positions[arr[i]] = i
    
    unique_elements.reverse()
    
    return len(unique_elements), unique_elements

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
result = remove_duplicates(n, arr)
print(result[0])
print(" ".join(map(str, result[1])))
