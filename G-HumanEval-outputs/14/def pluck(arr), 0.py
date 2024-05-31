
def pluck(arr):
    smallest_even_value = float('inf')
    smallest_even_index = -1

    for i in range(len(arr)):
        if arr[i] % 2 == 0 and arr[i] < smallest_even_value:
            smallest_even_value = arr[i]
            smallest_even_index = i

    if smallest_even_index == -1:
        return []
    else:
        return [smallest_even_value, smallest_even_index]

# Example usage
print(pluck([4,2,3]))  # Output: [2, 1]
print(pluck([1,2,3]))  # Output: [2, 1]
print(pluck([]))        # Output: []
print(pluck([5, 0, 3, 0, 4, 2]))  # Output: [0, 1]
