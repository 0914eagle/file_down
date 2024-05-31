
def smallest_change(arr):
    n = len(arr)
    count = 0
    for i in range(n//2):
        if arr[i] != arr[n-1-i]:
            count += 1
    return count

# Test cases
print(smallest_change([1,2,3,5,4,7,9,6]))  # 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))  # 1
print(smallest_change([1, 2, 3, 2, 1]))  # 0
